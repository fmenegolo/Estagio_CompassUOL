import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, substring, when, regexp_replace, expr, size
from pyspark.sql.types import StructType, StructField, StringType, FloatType, IntegerType
from datetime import datetime

  
sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)


# Definir o esquema para o DataFrame df_movies_IMDB
schema_movies_IMDB = StructType([
    StructField("id", StringType(), True),
    StructField("tituloPincipal", StringType(), True),
    StructField("tituloOriginal", StringType(), True),
    StructField("anoLancamento", StringType(), True),
    StructField("tempoMinutos", StringType(), True),
    StructField("genero", StringType(), True),
    StructField("notaMedia", FloatType(), True),  # Definir tipo como FloatType()
    StructField("numeroVotos", IntegerType(), True),  # Definir tipo como IntegerType()
    StructField("generoArtista", StringType(), True),
    StructField("personagem", StringType(), True),
    StructField("nomeArtista", StringType(), True),
    StructField("anoNascimento", StringType(), True),  
    StructField("anoFalecimento", StringType(), True),  
    StructField("profissao", StringType(), True),
    StructField("titulosMaisConhecidos", StringType(), True)
])

# Definir o esquema para o DataFrame df_series_IMDB
schema_series_IMDB = StructType([
    StructField("id", StringType(), True),
    StructField("tituloPincipal", StringType(), True),
    StructField("tituloOriginal", StringType(), True),
    StructField("anoLancamento", StringType(), True), 
    StructField("anoTermino", StringType(), True),  
    StructField("tempoMinutos", IntegerType(), True),  # Definir tipo como IntegerType()
    StructField("genero", StringType(), True),
    StructField("notaMedia", FloatType(), True),  # Definir tipo como FloatType()
    StructField("numeroVotos", IntegerType(), True),  # Definir tipo como IntegerType()
    StructField("generoArtista", StringType(), True),
    StructField("personagem", StringType(), True),
    StructField("nomeArtista", StringType(), True),
    StructField("anoNascimento", StringType(), True),  
    StructField("anoFalecimento", StringType(), True),  
    StructField("profissao", StringType(), True),
    StructField("titulosMaisConhecidos", StringType(), True)
])
# Define os caminhos dos arquivos no S3
path1 = "s3://data-lake-do-fabricio/Raw/Local/CSV/Movies/2023/05/02/"
path2 = "s3://data-lake-do-fabricio/Raw/Local/CSV/Series/2023/05/02/"
path3 = "s3://data-lake-do-fabricio/Raw/TMDB/JSON/Movies/2023/05/27/"
path4 = "s3://data-lake-do-fabricio/Raw/TMDB/JSON/Series/2023/05/27/"

# Carrega os DataFrames
df_movies_IMDB = spark.read.option("delimiter", "|").schema(schema_movies_IMDB).csv(path1 + 'movies.csv', header=True)
df_series_IMDB = spark.read.option("delimiter", "|").schema(schema_series_IMDB).csv(path2 + 'series.csv', header=True)
df_movies_TMDB = spark.read.json(path3 + 'movies_20230527_033040.json') 
df_series_TMDB = spark.read.json(path4 + 'series_20230527_033040.json')
df_movies_IMDB = df_movies_IMDB.withColumnRenamed("tituloPincipal", "tituloPrincipal")
df_series_IMDB = df_series_IMDB.withColumnRenamed("tituloPincipal", "tituloPrincipal")

# Converter a coluna 'title' do DataFrame JSON para um array de palavras e extrair o ano de lançamento
df_movies_TMDB_titulos_datas = df_movies_TMDB.select(
    regexp_replace(col('title'), r"[^a-zA-Z0-9\s]", "").alias('title_replaced'),
    substring(col('release_date'), 1, 4).alias('releaseDate')
)

# Aplicar substituição nos títulos
df_movies_IMDB = df_movies_IMDB.withColumn('tituloPrincipal_replaced', regexp_replace(col('tituloPrincipal'), r"[^a-zA-Z0-9\s]", ""))

# Realizar a filtragem dos títulos
df_movies_IMDB_trusted = df_movies_IMDB.join(df_movies_TMDB_titulos_datas,
    expr(
        "(size(split(tituloPrincipal_replaced, ' ')) = 1 AND " +
        "size(filter(split(tituloPrincipal_replaced, ' '), x -> length(x) > 4 AND instr(title_replaced, x) > 0)) >= 1) OR " +
        "(size(split(tituloPrincipal_replaced, ' ')) = 2 AND " +
        "size(filter(split(tituloPrincipal_replaced, ' '), x -> length(x) >= 1 AND instr(title_replaced, x) > 0)) >= 2) OR " +
        "(size(split(tituloPrincipal_replaced, ' ')) >= 3 AND " +
        "size(filter(split(tituloPrincipal_replaced, ' '), x -> length(x) > 3 AND instr(title_replaced, x) > 0)) >= 2)"
    ) &
    (df_movies_IMDB['anoLancamento'] == df_movies_TMDB_titulos_datas['releaseDate']) &
    (col('tituloPrincipal_replaced').isNotNull()) &
    (col('tituloPrincipal_replaced') != '') &
    (col('title_replaced').isNotNull()) &
    (col('title_replaced') != ''),
    'inner')

# Remover as colunas 'title' e 'releaseDate' do DataFrame
df_movies_IMDB_trusted = df_movies_IMDB_trusted.drop('title_replaced', 'releaseDate')

# Trata os valores "NA" na coluna
df_movies_IMDB_trusted = df_movies_IMDB_trusted.withColumn("anoFalecimento", when(col("anoFalecimento") == "\\N", None).otherwise(col("anoFalecimento")))
df_movies_IMDB_trusted = df_movies_IMDB_trusted.withColumn("anoNascimento", when(col("anoNascimento") == "\\N", None).otherwise(col("anoNascimento")))
df_movies_IMDB_trusted = df_movies_IMDB_trusted.withColumn("tempoMinutos", when(col("tempoMinutos") == "\\N", None).otherwise(col("tempoMinutos")))
df_movies_IMDB_trusted = df_movies_IMDB_trusted.withColumn("notaMedia", when(col("notaMedia") == "\\N", None).otherwise(col("notaMedia")))
df_movies_IMDB_trusted = df_movies_IMDB_trusted.withColumn("numeroVotos", when(col("numeroVotos") == "\\N", None).otherwise(col("numeroVotos")))

# Elimina possiveis Redundâncias
df_movies_IMDB_trusted = df_movies_IMDB_trusted.distinct()

# Converter a coluna 'name' e a substring de 'first_air_date' do DataFrame JSON para o DataFrame do TMDB
df_series_TMDB_titulos_datas = df_series_TMDB.select(regexp_replace(col('name'), r"[^a-zA-Z0-9\s]", "").alias('title_replaced'),
    substring(col('first_air_date'), 1, 4).alias('releaseDate'))

# Aplicar substituição nos títulos
df_series_IMDB = df_series_IMDB.withColumn('tituloPrincipal_replaced', regexp_replace(col('tituloPrincipal'), r"[^a-zA-Z0-9\s]", ""))

# Realizar a filtragem dos títulos e anos de lançamento

df_series_IMDB_layer1 = df_series_IMDB.join(df_series_TMDB_titulos_datas,
    expr(
        "(size(split(tituloPrincipal_replaced, ' ')) = 1 AND " +
        "size(filter(split(tituloPrincipal_replaced, ' '), x -> length(x) > 3 AND instr(title_replaced, x) > 0)) >= 1) OR " +
        "(size(split(tituloPrincipal_replaced, ' ')) = 2 AND " +
        "size(filter(split(tituloPrincipal_replaced, ' '), x -> length(x) >= 1 AND instr(title_replaced, x) > 0)) >= 2) OR " +
        "(size(split(tituloPrincipal_replaced, ' ')) >= 3 AND " +
        "size(filter(split(tituloPrincipal_replaced, ' '), x -> length(x) > 3 AND instr(title_replaced, x) > 0)) >= 2)"
    ) &
    (df_series_IMDB['anoLancamento'] == df_series_TMDB_titulos_datas['releaseDate']) &
    (col('tituloPrincipal_replaced').isNotNull()) &
    (col('tituloPrincipal_replaced') != '') &
    (col('title_replaced').isNotNull()) &
    (col('title_replaced') != ''),
    'inner')

# Remover as colunas 'title' e 'releaseDate' do DataFrame
df_series_IMDB_layer1 = df_series_IMDB_layer1.drop('title_replaced', 'releaseDate')

# Trata os valores "NA" na coluna
df_series_IMDB_layer1 = df_series_IMDB_layer1.withColumn("anoTermino", when(col("anoTermino") == "\\N", None).otherwise(col("anoTermino")))
df_series_IMDB_layer1 = df_series_IMDB_layer1.withColumn("tempoMinutos", when(col("tempoMinutos") == "\\N", None).otherwise(col("tempoMinutos")))
df_series_IMDB_layer1 = df_series_IMDB_layer1.withColumn("notaMedia", when(col("notaMedia") == "\\N", None).otherwise(col("notaMedia")))
df_series_IMDB_layer1 = df_series_IMDB_layer1.withColumn("numeroVotos", when(col("numeroVotos") == "\\N", None).otherwise(col("numeroVotos")))
df_series_IMDB_layer1 = df_series_IMDB_layer1.withColumn("anoNascimento", when(col("anoNascimento") == "\\N", None).otherwise(col("anoNascimento")))
df_series_IMDB_layer1 = df_series_IMDB_layer1.withColumn("anoFalecimento", when(col("anoFalecimento") == "\\N", None).otherwise(col("anoFalecimento")))
df_series_IMDB_layer1 = df_series_IMDB_layer1.withColumn("anoFalecimento", when(col("anoFalecimento") == "\\N", None).otherwise(col("anoFalecimento")))

# Elimina possiveis Redundâncias
df_series_IMDB_layer1 = df_series_IMDB_layer1.distinct()


# Aplicar substituição nos títulos
df_series_TMDB = df_series_TMDB.withColumn('name_replaced', regexp_replace(col('name'), r"[^a-zA-Z0-9\s]", ""))

# Realizar a filtragem dos títulos
df_series_TMDB_trusted = df_series_TMDB.join(df_movies_TMDB_titulos_datas,
    expr(
        "(size(split(name_replaced, ' ')) = 1 AND " +
        "size(filter(split(name_replaced, ' '), x -> length(x) > 4 AND instr(title_replaced, x) > 0)) >= 1) OR " +
        "(size(split(name_replaced, ' ')) = 2 AND " +
        "size(filter(split(name_replaced, ' '), x -> length(x) >= 1 AND instr(title_replaced, x) > 0)) >= 2) OR " +
        "(size(split(name_replaced, ' ')) >= 3 AND " +
        "size(filter(split(name_replaced, ' '), x -> length(x) > 3 AND instr(title_replaced, x) > 0)) >= 2)"
    ) &
    (col('name_replaced').isNotNull()) &
    (col('name_replaced') != '') &
    (col('title_replaced').isNotNull()) &
    (col('title_replaced') != ''),
    'inner')

# Retira colunas irrelevantes
df_series_TMDB_trusted = df_series_TMDB_trusted.drop('titulo','backdrop_path','poster_path','title_replaced','releaseDate')

# Trata os valores "NA" nas colunas
df_series_TMDB_trusted = df_series_TMDB_trusted.withColumn("first_air_date", when(col("first_air_date") == "", None).otherwise(col("first_air_date")))
df_series_TMDB_trusted = df_series_TMDB_trusted.withColumn("genre_ids", when(size(col("genre_ids")) == 0, None).otherwise(col("genre_ids")))
df_series_TMDB_trusted = df_series_TMDB_trusted.withColumn("overview", when(col("overview") == "", None).otherwise(col("overview")))
df_series_TMDB_trusted = df_series_TMDB_trusted.withColumn("popularity", when(col("popularity") == "", None).otherwise(col("popularity")))
df_series_TMDB_trusted = df_series_TMDB_trusted.withColumn("vote_average", when(col("vote_average") == "", None).otherwise(col("vote_average")))
df_series_TMDB_trusted = df_series_TMDB_trusted.withColumn("vote_count", when(col("vote_count") == "", None).otherwise(col("vote_count")))

# Elimina possiveis Redundâncias
df_series_TMDB_trusted = df_series_TMDB_trusted.distinct()

# Converter a coluna 'title' do DataFrame JSON para um array de palavras e extrair o ano de lançamento
df_series_TMDB_titulos_datas = df_series_TMDB_trusted.select(regexp_replace(col('name'), r"[^a-zA-Z0-9\s]", "").alias('title_replaced'),
    substring(col('first_air_date'), 1, 4).alias('releaseDate'))

# Realizar a filtragem dos títulos e anos de lançamento
df_series_IMDB_trusted = df_series_IMDB_layer1.join(df_series_TMDB_titulos_datas,
    expr(
        "(size(split(tituloPrincipal_replaced, ' ')) = 1 AND " +
        "size(filter(split(tituloPrincipal_replaced, ' '), x -> length(x) > 3 AND instr(title_replaced, x) > 0)) >= 1) OR " +
        "(size(split(tituloPrincipal_replaced, ' ')) = 2 AND " +
        "size(filter(split(tituloPrincipal_replaced, ' '), x -> length(x) >= 1 AND instr(title_replaced, x) > 0)) >= 2) OR " +
        "(size(split(tituloPrincipal_replaced, ' ')) >= 3 AND " +
        "size(filter(split(tituloPrincipal_replaced, ' '), x -> length(x) > 3 AND instr(title_replaced, x) > 0)) >= 2)"
    ) &
    (df_series_IMDB['anoLancamento'] == df_series_TMDB_titulos_datas['releaseDate']) &
    (col('tituloPrincipal_replaced').isNotNull()) &
    (col('tituloPrincipal_replaced') != '') &
    (col('title_replaced').isNotNull()) &
    (col('title_replaced') != ''),
    'inner')

# Retira colunas irrelevantes (somete para versão AWS)
df_series_IMDB_layer1 = df_series_IMDB_layer1.drop('title_replaced', 'releaseDate')

# Trata os valores "NA" nas colunas
df_series_IMDB_trusted = df_series_IMDB_trusted.withColumn("anoTermino", when(col("anoTermino") == "\\N", None).otherwise(col("anoTermino")))
df_series_IMDB_trusted = df_series_IMDB_trusted.withColumn("tempoMinutos", when(col("tempoMinutos") == "\\N", None).otherwise(col("tempoMinutos")))
df_series_IMDB_trusted = df_series_IMDB_trusted.withColumn("genero", when(col("genero") == "\\N", None).otherwise(col("genero")))
df_series_IMDB_trusted = df_series_IMDB_trusted.withColumn("notaMedia", when(col("notaMedia") == "\\N", None).otherwise(col("notaMedia")))
df_series_IMDB_trusted = df_series_IMDB_trusted.withColumn("numeroVotos", when(col("numeroVotos") == "\\N", None).otherwise(col("numeroVotos")))
df_series_IMDB_trusted = df_series_IMDB_trusted.withColumn("anoNascimento", when(col("anoNascimento") == "\\N", None).otherwise(col("anoNascimento")))
df_series_IMDB_trusted = df_series_IMDB_trusted.withColumn("anoNascimento", when(col("anoNascimento") == "\\N", None).otherwise(col("anoNascimento")))
df_series_IMDB_trusted = df_series_IMDB_trusted.withColumn("anoFalecimento", when(col("anoFalecimento") == "\\N", None).otherwise(col("anoFalecimento")))

# Remover linhas duplicadas no resultado
df_series_IMDB_trusted = df_series_IMDB_trusted.distinct()

# remove os colunas não relevantes
df_movies_TMDB_trusted = df_movies_TMDB.drop('adult','backdrop_path','poster_path','video')

# Trata os valores "NA" na coluna
df_movies_TMDB_trusted = df_movies_TMDB_trusted.withColumn("popularity", when(col("popularity") == "", None).otherwise(col("popularity")))
df_movies_TMDB_trusted = df_movies_TMDB_trusted.withColumn("vote_average", when(col("vote_average") == "", None).otherwise(col("vote_average")))
df_movies_TMDB_trusted = df_movies_TMDB_trusted.withColumn("vote_count", when(col("vote_count") == "", None).otherwise(col("vote_count")))

# altera schema das colunas do DF TMDB
df_movies_TMDB_trusted = df_movies_TMDB_trusted.withColumn("popularity", col("popularity").cast(FloatType()))
df_movies_TMDB_trusted = df_movies_TMDB_trusted.withColumn("vote_average", col("vote_average").cast(FloatType()))
df_movies_TMDB_trusted = df_movies_TMDB_trusted.withColumn("vote_count", col("vote_count").cast(IntegerType()))
df_series_TMDB_trusted = df_series_TMDB_trusted.withColumn("popularity", col("popularity").cast(FloatType()))
df_series_TMDB_trusted = df_series_TMDB_trusted.withColumn("vote_average", col("vote_average").cast(FloatType()))
df_series_TMDB_trusted = df_series_TMDB_trusted.withColumn("vote_count", col("vote_count").cast(IntegerType()))

# Obtém a data atual para criar os diretórios correspondentes
current_date = datetime.now()
ano = current_date.strftime("%Y")
mes = current_date.strftime("%m")
dia = current_date.strftime("%d")

# Define os caminhos de destino no S3 para os DataFrames no formato Parquet
path_trt_local_movies = "s3://data-lake-do-fabricio/TRT/Local/Parquet/Movies/{ano}/{mes}/{dia}/"
path_trt_local_series = "s3://data-lake-do-fabricio/TRT/Local/Parquet/Series/{ano}/{mes}/{dia}/"
path_trt_tmdb_movies = "s3://data-lake-do-fabricio/TRT/TMDB/Parquet/Movies/{ano}/{mes}/{dia}/"
path_trt_tmdb_series = "s3://data-lake-do-fabricio/TRT/TMDB/Parquet/Series/{ano}/{mes}/{dia}/"

# Salva os DataFrames no formato Parquet no S3
df_movies_IMDB_trusted.write.parquet(path_trt_local_movies.format(ano=ano, mes=mes, dia=dia))
df_series_IMDB_trusted.write.parquet(path_trt_local_series.format(ano=ano, mes=mes, dia=dia))
df_movies_TMDB_trusted.write.parquet(path_trt_tmdb_movies.format(ano=ano, mes=mes, dia=dia))
df_series_TMDB_trusted.write.parquet(path_trt_tmdb_series.format(ano=ano, mes=mes, dia=dia))

# Finaliza o Job
job.commit()