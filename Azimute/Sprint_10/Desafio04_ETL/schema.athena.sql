CREATE EXTERNAL TABLE IF NOT EXISTS `Dash`.`movies_tb` (
  `id` int,
  `movie_id` varchar(20),
  `genre_ids` array < int >,
  `title` varchar(100),
  `tempoMinutos` varchar(10),
  `release_date` varchar(20),
  `original_language` varchar(10),
  `popularity` varchar(10),
  `nota_media` varchar(5),
  `votos` int
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION 's3://data-lake-do-fabricio/Refined/Parquet/Movies/'
TBLPROPERTIES ('classification' = 'parquet');


CREATE EXTERNAL TABLE IF NOT EXISTS `dash`.`series_tb` (
  `id` int,
  `seriesId` varchar(20),
  `genre_ids` array < int >,
  `name` varchar(100),
  `tempoMinutos` int,
  `first_air_date` varchar(20),
  `anoTermino` varchar(5),
  `original_language` varchar(5),
  `popularity` varchar(10),
  `nota_media` varchar(5),
  `votos` int
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION 's3://data-lake-do-fabricio/Refined/Parquet/Series/'
TBLPROPERTIES ('classification' = 'parquet');


CREATE EXTERNAL TABLE IF NOT EXISTS `dash`.`actors_tb` (
  `id` varchar(20),
  `personagem` varchar(100),
  `nomeArtista` varchar(100),
  `generoArtista` varchar(15),
  `anoNascimento` varchar(5),
  `anoFalecimento` varchar(5),
  `profissao` array < string >,
  `titulosMaisConhecidos` array < string >
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
STORED AS INPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION 's3://data-lake-do-fabricio/Refined/Parquet/Actors/'
TBLPROPERTIES ('classification' = 'parquet');