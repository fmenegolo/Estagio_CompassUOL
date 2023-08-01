import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, substring, regexp_replace, expr, size, levenshtein, avg, when, format_number, sum, lower, trim, split, dense_rank
from pyspark.sql import functions as F
from pyspark.sql.window import Window
from datetime import datetime

  
sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)



# Define os caminhos dos arquivos no S3
path1 = "s3://data-lake-do-fabricio/TRT/Local/Parquet/Movies/2023/06/05/"
path2 = "s3://data-lake-do-fabricio/TRT/Local/Parquet/Series/2023/06/05/"
path3 = "s3://data-lake-do-fabricio/TRT/TMDB/Parquet/Movies/2023/06/05/"
path4 = "s3://data-lake-do-fabricio/TRT/TMDB/Parquet/Series/2023/06/05/"
# Carrega os DataFrames
df_movies_IMDB_trusted = spark.read.parquet(path1 + '*.parquet')
df_series_IMDB_trusted = spark.read.parquet(path2 + '*.parquet')
df_movies_TMDB_trusted = spark.read.parquet(path3 + '*.parquet')
df_series_TMDB_trusted = spark.read.parquet(path4 + '*.parquet')
df_movies_IMDB = df_movies_IMDB_trusted.select("id", "tituloPrincipal", "tituloOriginal", "anoLancamento", "tempoMinutos", "genero", "notaMedia", "numeroVotos")
df_movies_IMDB = df_movies_IMDB.dropDuplicates(['id'])  # Remover duplicatas pelo ID
df_movies_IMDB = df_movies_IMDB.withColumnRenamed("id", "movie_id")  # Renomear a coluna "id" para "movie_id"
df_series_IMDB = df_series_IMDB_trusted.select("id", "tituloPrincipal", "tituloOriginal", "anoLancamento", "anoTermino", "tempoMinutos", "genero", "notaMedia", "numeroVotos")
df_series_IMDB = df_series_IMDB.dropDuplicates(['id'])  # Remover duplicatas pelo ID
df_series_IMDB = df_series_IMDB.withColumnRenamed("id", "seriesId")  # Renomear a coluna "id" para "movie_id"
# Aplicar regexp_replace no dataframe df_movies_TMDB
df_movies_TMDB_titulos_datas = df_movies_TMDB_trusted.select(
    regexp_replace(col('title'), r"[^a-zA-Z0-9\s]", "").alias('title_replaced'),
    substring(col('release_date'), 1, 4).alias('releaseDate'),
    col('id'),
    col('genre_ids'),
    col('original_language'),
    col('popularity'),
    col('vote_average'),
    col('vote_count'),
    col('title'),
    col('release_date')
)

# Aplicar regexp_replace no dataframe df_movies_IMDB
df_movies_IMDB_titulos_datas = df_movies_IMDB.select(
    regexp_replace(col('tituloPrincipal'), r"[^a-zA-Z0-9\s]", "").alias('tituloPrincipal_replaced'),
    substring(col('anoLancamento'), 1, 4).alias('anoLancamento'),
    col('movie_id'),
    col('tituloOriginal'),
    col('tempoMinutos'),
    col('genero'),
    col('notaMedia'),
    col('numeroVotos')
)

# Remover a sentença "Final Chapter Part" do dataframe df_movies_IMDB
df_movies_IMDB_titulos_datas = df_movies_IMDB_titulos_datas.withColumn('tituloPrincipal_replaced', regexp_replace(col('tituloPrincipal_replaced'), 'Final Chapter Part', '')
)

# Realizar a comparação de similaridade entre os títulos dos dataframes e filtrar pelo ano de lançamento
df_movies_refined = df_movies_TMDB_titulos_datas.join(
    df_movies_IMDB_titulos_datas,
    expr(
        "(size(split(title_replaced, ' ')) = 1 AND " +
        "size(filter(split(title_replaced, ' '), x -> length(x) > 3 AND instr(tituloPrincipal_replaced, x) > 0)) >= 1) OR " +
        "(size(split(title_replaced, ' ')) = 2 AND " +
        "size(filter(split(title_replaced, ' '), x -> length(x) >= 1 AND instr(tituloPrincipal_replaced, x) > 0)) >= 2) OR " +
        "(size(split(title_replaced, ' ')) = 3 AND " +
        "size(filter(split(title_replaced, ' '), x -> length(x) > 3 AND instr(tituloPrincipal_replaced, x) > 0)) >= 2) OR " +
        "(size(split(title_replaced, ' ')) = 4 AND " +
        "size(filter(split(title_replaced, ' '), x -> length(x) > 3 AND instr(tituloPrincipal_replaced, x) > 0)) >= 3) OR " +
        "(size(split(title_replaced, ' ')) >= 5 AND " +
        "size(filter(split(title_replaced, ' '), x -> length(x) >= 3 AND instr(tituloPrincipal_replaced, x) > 0)) >= 3 AND " +
        "levenshtein(tituloPrincipal_replaced, title_replaced) <= 9)"
    ) &
    (df_movies_TMDB_titulos_datas['releaseDate'] == df_movies_IMDB_titulos_datas['anoLancamento']) &
    (col('tituloPrincipal_replaced').isNotNull()) &
    (col('tituloPrincipal_replaced') != '') &
    (col('title_replaced').isNotNull()) &
    (col('title_replaced') != ''),
    'left_outer'
)

# Calcular a soma de vote_count e numeroVotos (se não forem nulos)
df_movies_refined = df_movies_refined.withColumn('votos', col('vote_count') + col('numeroVotos'))

# Calcular a média de vote_average e notaMedia (se não forem nulos)
df_movies_refined = df_movies_refined.withColumn('nota_media', when(
    col('vote_count').isNotNull() & col('numeroVotos').isNotNull(),
    (col('vote_average') * col('vote_count') + col('notaMedia') * col('numeroVotos')) / col('votos')
).otherwise(
    when(col('vote_count').isNotNull(), col('vote_average')).otherwise(col('notaMedia'))
))

# Tratar valores nulos e arredondar a nota média ponderada para uma casa decimal
df_movies_refined = df_movies_refined.withColumn('votos', when(col('votos').isNull(), col('vote_count')).otherwise(col('votos')))
df_movies_refined = df_movies_refined.withColumn('nota_media', when(col('nota_media').isNull(), col('vote_average')).otherwise(col('nota_media')))
df_movies_refined = df_movies_refined.withColumn('nota_media', format_number(col('nota_media'), 1))

# Apagar as colunas indesejadas
df_movies_refined = df_movies_refined.drop('releaseDate', 'tituloPrincipal_replaced', 'anoLancamento', 'title_replaced','vote_average','vote_count','notaMedia','numeroVotos','tituloOriginal','genero')

# Remover caracteres especiais que não sejam letras acentuadas na coluna "title"
df_movies_refined = df_movies_refined.withColumn("title", regexp_replace(df_movies_refined["title"], "[^a-zA-ZÀ-ÿ, ]", ""))

# Selecione apenas as colunas desejadas
df_movies_refined = df_movies_refined.select('id','movie_id','genre_ids', 'title', 'tempoMinutos', 'release_date', 'original_language', 'popularity', 'nota_media', 'votos')

df_movies_refined = df_movies_refined.distinct()

# Aplicar regexp_replace no dataframe df_series_TMDB

df_series_TMDB_titulos_datas = df_series_TMDB_trusted.select(
    substring(col('first_air_date'), 1, 4).alias('releaseDate'),
    col('name_replaced'),
    col('id'),
    col('genre_ids'),
    col('original_language'),
    col('popularity'),
    col('vote_average'),
    col('vote_count'),
    col('name'),
    col('first_air_date')
)

# dataframe df_movies_TMDB
df_movies_TMDB_titulos_datas = df_movies_TMDB_titulos_datas.select(col('title_replaced'))

# Realizar a comparação de similaridade entre os títulos dos dataframes e filtrar pelo ano de lançamento
df_series_TMDB_Layer1 = df_series_TMDB_titulos_datas.join(
    df_movies_TMDB_titulos_datas,
    expr(
        "(size(split(name_replaced, ' ')) = 1 AND " +
        "size(filter(split(name_replaced, ' '), x -> length(x) > 3 AND instr(title_replaced, x) > 0)) >= 1) OR " +
        "(size(split(name_replaced, ' ')) = 2 AND " +
        "size(filter(split(name_replaced, ' '), x -> length(x) >= 1 AND instr(title_replaced, x) > 0)) >= 2) OR " +
        "(size(split(name_replaced, ' ')) = 3 AND " +
        "size(filter(split(name_replaced, ' '), x -> length(x) > 3 AND instr(title_replaced, x) > 0)) >= 2) OR " +
        "(size(split(name_replaced, ' ')) = 4 AND " +
        "size(filter(split(name_replaced, ' '), x -> length(x) > 3 AND instr(title_replaced, x) > 0)) >= 3) OR " +
        "(size(split(name_replaced, ' ')) >= 5 AND " +
        "size(filter(split(name_replaced, ' '), x -> length(x) >= 3 AND instr(title_replaced, x) > 0)) >= 3 AND " +
        "levenshtein(title_replaced, name_replaced) <= 8)"
    ) &
    (col('title_replaced').isNotNull()) &
    (col('title_replaced') != '') &
    (col('name_replaced').isNotNull()) &
    (col('name_replaced') != ''),
    'inner'
)

# Apagar as colunas indesejadas
df_series_TMDB_Layer1 = df_series_TMDB_Layer1.drop('title_replaced')

# Aplicar regexp_replace no dataframe df_movies_IMDB
df_series_IMDB_titulos_datas = df_series_IMDB.select(
    regexp_replace(col('tituloPrincipal'), r"[^a-zA-Z0-9\s]", "").alias('tituloPrincipal_replaced'),
    substring(col('anoLancamento'), 1, 4).alias('anoLancamento'),
    col('seriesId'),
    col('tituloPrincipal'),
    col('tempoMinutos'),
    col('anoTermino'),
    col('notaMedia'),
    col('numeroVotos')
)

# Realizar a comparação de similaridade entre os títulos dos dataframes e filtrar pelo ano de lançamento
df_series_refined = df_series_TMDB_Layer1.join(
    df_series_IMDB_titulos_datas,
    expr(
        "(size(split(name_replaced, ' ')) = 1 AND " +
        "size(filter(split(name_replaced, ' '), x -> length(x) > 3 AND instr(tituloPrincipal_replaced, x) > 0)) >= 1) OR " +
        "(size(split(name_replaced, ' ')) = 2 AND " +
        "size(filter(split(name_replaced, ' '), x -> length(x) >= 1 AND instr(tituloPrincipal_replaced, x) > 0)) >= 2) OR " +
        "(size(split(name_replaced, ' ')) = 3 AND " +
        "size(filter(split(name_replaced, ' '), x -> length(x) > 3 AND instr(tituloPrincipal_replaced, x) > 0)) >= 2) OR " +
        "(size(split(name_replaced, ' ')) = 4 AND " +
        "size(filter(split(name_replaced, ' '), x -> length(x) > 3 AND instr(tituloPrincipal_replaced, x) > 0)) >= 3) OR " +
        "(size(split(name_replaced, ' ')) >= 5 AND " +
        "size(filter(split(name_replaced, ' '), x -> length(x) >= 3 AND instr(tituloPrincipal_replaced, x) > 0)) >= 3 AND " +
        "levenshtein(tituloPrincipal_replaced, name_replaced) <= 9)"
    ) &
    (df_series_TMDB_Layer1['releaseDate'] == df_series_IMDB_titulos_datas['anoLancamento']) &
    (col('tituloPrincipal_replaced').isNotNull()) &
    (col('tituloPrincipal_replaced') != '') &
    (col('name_replaced').isNotNull()) &
    (col('name_replaced') != ''),
    'left_outer'
)

# Criar colunas com a soma dos votos e a média ponderada
df_series_refined = df_series_refined.withColumn('votos', col('vote_count') + col('numeroVotos'))

df_series_refined = df_series_refined.withColumn('nota_media', when(
    col('vote_count').isNotNull() & col('numeroVotos').isNotNull(),
    (col('vote_average') * col('vote_count') + col('notaMedia') * col('numeroVotos')) / col('votos')
).otherwise(
    when(col('vote_count').isNotNull(), col('vote_average')).otherwise(col('notaMedia'))
))

# Tratar valores nulos e arredondar a nota média ponderada para uma casa decimal
df_series_refined = df_series_refined.withColumn('votos', when(col('votos').isNull(), col('vote_count')).otherwise(col('votos')))
df_series_refined = df_series_refined.withColumn('nota_media', when(col('nota_media').isNull(), col('vote_average')).otherwise(col('nota_media')))
df_series_refined = df_series_refined.withColumn('nota_media', format_number(col('nota_media'), 1))

# Apagar as colunas indesejadas
df_series_refined = df_series_refined.drop('releaseDate', 'tituloPrincipal_replaced', 'releaseDate', 'name_replaced','vote_average','vote_count','notaMedia','numeroVotos','tituloPrincipal','anoLancamento')

# Remover caracteres especiais que não sejam letras acentuadas na coluna "name"
df_series_refined = df_series_refined.withColumn("name", regexp_replace(df_series_refined["name"], "[^a-zA-ZÀ-ÿ, ]", ""))

# Selecione apenas as colunas linhas desejadas
df_series_refined = df_series_refined.select('id','seriesId','genre_ids', 'name', 'tempoMinutos', 'first_air_date', 'anoTermino', 'original_language', 'popularity', 'nota_media', 'votos')
df_series_refined = df_series_refined.distinct()

# Cria DF Actors
df_movies_actors = df_movies_IMDB_trusted.select("id", "personagem", "nomeArtista", "generoArtista", "anoNascimento", "anoFalecimento", "profissao", "titulosMaisConhecidos")
df_series_actors = df_series_IMDB_trusted.select("id", "personagem", "nomeArtista", "generoArtista", "anoNascimento", "anoFalecimento", "profissao", "titulosMaisConhecidos")

# Obter a lista de film_ids presentes na tabela de filmes selecionados
filme_ids = df_movies_refined.select("movie_id")
serie_ids = df_series_refined.select("seriesId")

# Realizar o join entre os DataFrames
df_movies_actors = df_movies_actors.join(filme_ids, df_movies_actors["id"] == filme_ids["movie_id"], "inner")
df_series_actors = df_series_actors.join(serie_ids, df_series_actors["id"] == serie_ids["seriesId"], "inner")

# Apaga coluna desnecessaria
df_movies_actors = df_movies_actors.drop("movie_id")
df_series_actors = df_series_actors.drop("seriesId")

# Apaga dados repetidos
df_movies_actors = df_movies_actors.distinct()
df_series_actors = df_series_actors.distinct()

# Unir df Atores de filmes e series
df_actors = df_movies_actors.unionAll(df_series_actors)

# Atualizar os dados da coluna com regex_replace pois dubladores atuam com mais de um pesonagem e os nomes estão unidos em camelCase
df_actors = df_actors.withColumn("personagem", regexp_replace(df_actors["personagem"], "([a-z])([A-Z])", "$1 $2"))
df_actors = df_actors.withColumn("nomeArtista", regexp_replace(df_actors["nomeArtista"], "([a-z])([A-Z])", "$1 $2"))

# Remover palavras repetidas dentro de cada célula da coluna "personagem"
df_actors = df_actors.withColumn("personagem", expr("regexp_replace(personagem, '\\b(\\w+)\\b\\s+\\1\\b', '$1')"))

# Remover conteúdo entre parênteses da coluna "personagem"
df_actors = df_actors.withColumn("personagem", regexp_replace(df_actors["personagem"], r'\([^()]*\)', ''))

# Substituir letras acentuadas por suas versões não acentuadas na coluna "personagem"
df_actors = df_actors.withColumn("personagem", regexp_replace(df_actors["personagem"], "[áàâãä]", "a"))
df_actors = df_actors.withColumn("personagem", regexp_replace(df_actors["personagem"], "[éèêë]", "e"))
df_actors = df_actors.withColumn("personagem", regexp_replace(df_actors["personagem"], "[íìîï]", "i"))
df_actors = df_actors.withColumn("personagem", regexp_replace(df_actors["personagem"], "[óòôõö]", "o"))
df_actors = df_actors.withColumn("personagem", regexp_replace(df_actors["personagem"], "[úùûü]", "u"))
df_actors = df_actors.withColumn("personagem", regexp_replace(df_actors["personagem"], "[ç]", "c"))

# Remover a palavra "Son" do início do nome na coluna "personagem"
df_actors = df_actors.withColumn("personagem", regexp_replace(df_actors["personagem"], "^Son ", ""))

# Atribua IDs únicos para artistas com nomes repetidos
window = Window.partitionBy("nomeArtista").orderBy("id")
df_actors = df_actors.withColumn("IdArtista", dense_rank().over(window))

# Atualizar o formato da coluna 'profissao'
df_actors = df_actors.withColumn('profissao', split(regexp_replace(df_actors['profissao'], ',\\s*', ','), ','))

# Atualizar o formato da coluna 'titulosMaisConhecidos'
df_actors = df_actors.withColumn('titulosMaisConhecidos', split(regexp_replace(df_actors['titulosMaisConhecidos'], ',\\s*', ','), ','))

df_movies_refined.createOrReplaceTempView("movies")
df_series_refined.createOrReplaceTempView("series")
df_actors.createOrReplaceTempView("actors")

# Obtém a data atual para criar os diretórios correspondentes
current_date = datetime.now()
ano = current_date.strftime("%Y")
mes = current_date.strftime("%m")
dia = current_date.strftime("%d")

# Define os caminhos de destino no S3 para os DataFrames no formato Parquet
path_ref_movies = "s3://data-lake-do-fabricio/Refined/Parquet/Movies/{ano}/{mes}/{dia}/"
path_ref_series = "s3://data-lake-do-fabricio/Refined/Parquet/Series/{ano}/{mes}/{dia}/"
path_ref_actors = "s3://data-lake-do-fabricio/Refined/Parquet/Actors/{ano}/{mes}/{dia}/"

# Salva os DataFrames no formato Parquet no S3
df_movies_refined.write.parquet(path_ref_movies.format(ano=ano, mes=mes, dia=dia))
df_series_refined.write.parquet(path_ref_series.format(ano=ano, mes=mes, dia=dia))
df_actors.write.parquet(path_ref_actors.format(ano=ano, mes=mes, dia=dia))


job.commit()