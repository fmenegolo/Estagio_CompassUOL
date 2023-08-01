-- Criação da view movies_dim
CREATE OR REPLACE VIEW movies_dim AS
SELECT
  id AS movie_id,
  genre_ids,
  title,
  tempoMinutos,
  release_date,
  original_language,
  popularity,
  CAST(nota_media AS DOUBLE) AS nota_media,
  votos
FROM Dash.movies_tb;

-- Criação da view series_dim
CREATE OR REPLACE VIEW series_dim AS
SELECT
  id AS series_id,
  genre_ids,
  name,
  tempoMinutos,
  first_air_date,
  anoTermino,
  original_language,
  popularity,
  CAST(nota_media AS DOUBLE) AS nota_media,
  votos
FROM dash.series_tb;

-- Criação da view actors_dim
CREATE OR REPLACE VIEW actors_dim AS
SELECT
  id AS actor_id,
  personagem,
  nomeArtista,
  generoArtista,
  CAST(anoNascimento AS INT) AS anoNascimento,
  CAST(anoFalecimento AS INT) AS anoFalecimento,
  profissao,
  titulosMaisConhecidos
FROM dash.actors_tb;

-- Criação da view fato_actors_movies
CREATE OR REPLACE VIEW movies_series_combined_dim AS
SELECT
  id,
  movie_id AS Id_IMDB,
  genre_ids,
  title,
  CAST(tempoMinutos AS int) AS tempoMinutos,
  release_date AS dataLancamento,
  original_language,
  popularity,
  nota_media,
  votos,
  'Filme' AS tipo
FROM
  Dash.movies_tb
UNION ALL
SELECT
  id,
  seriesId AS Id_IMDB,
  genre_ids,
  name AS title,
  tempoMinutos,
  first_air_date AS dataLancamento,
  original_language,
  popularity,
  nota_media,
  votos,
  'Série' AS tipo
FROM
  dash.series_tb;


CREATE OR REPLACE VIEW "movies_series_actors_dim" AS 
SELECT
  a.id actor_id
, a.personagem
, a.nomeArtista
, a.generoArtista
, a.anoNascimento
, a.anoFalecimento
, a.profissao
, a.titulosMaisConhecidos
, mscv.id_IMDB movie_series_id
, mscv.genre_ids
, mscv.title
, mscv.tempoMinutos
, mscv.dataLancamento
, mscv.original_language
, mscv.popularity
, mscv.nota_media
, mscv.votos
, mscv.tipo
FROM
  (dash.actors_tb a
RIGHT JOIN movies_series_combined_dim mscv ON (a.id = mscv.id_IMDB))
