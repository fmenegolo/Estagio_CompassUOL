import boto3
import requests
import json
from datetime import datetime

s3 = boto3.resource('s3')
bucket_name = 'data-lake-do-fabricio'
raw_prefix = 'Raw/TMDB/JSON'

def lambda_handler(event, context):
    
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    
    movies_url = f'https://api.themoviedb.org/3/discover/movie?with_keywords=285442'
    series_url = f'https://api.themoviedb.org/3/discover/tv?with_keywords=210024%252C13141&with_original_language=ja'

    headers = {
        "accept": "application/json",
        'Authorization': "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYjgwMjA3ODgxYmYwNGNjYjlhMzI1OGMxZjEyODFlMSIsInN1YiI6IjY0NTNmNTRmODdhMjdhMDE1NDMyNWM2MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.9tYrFHogchw7N6x09PQ4zJTeTz8wGKOqn5dy6LYVQgw"
    }
    
    
    # No Loop para Verifica se existe mais paginas e retorna o resultado de todas elas
    movies = []
    page = 1
    while True:
        # Requisição na API para obter dados dos filmes
        response = requests.get(f'{movies_url}&page={page}', headers=headers)
        data = json.loads(response.text)
        movies_data = data.get('results')
        if movies_data:
            movies.extend(movies_data)
            page += 1
        else:
            break


    # Salvando dados dos filmes em arquivo JSON no S3
    movies_file = f'movies_{now.strftime("%Y%m%d_%H%M%S")}.json'
    movies_path = f'{raw_prefix}/Movies/{year}/{month}/{day}/{movies_file}'
    s3.Object(bucket_name, movies_path).put(Body=json.dumps(movies))
    
    
    # No Loop para Verifica se existe mais paginas e retorna o resultado de todas elas
    series = []
    page = 1
    while True:
        # Requisição na API para obter dados das séries de TV
        response = requests.get(f'{series_url}&page={page}', headers=headers)
        data = json.loads(response.text)
        series_data = data.get('results')
        if series_data is not None:
            series.extend(series_data)
            page += 1
        else:
            break    
    
    # Salvando dados das séries em arquivo JSON no S3
    series_file = f'series_{now.strftime("%Y%m%d_%H%M%S")}.json'
    series_path = f'{raw_prefix}/Series/{year}/{month}/{day}/{series_file}'
    s3.Object(bucket_name, series_path).put(Body=json.dumps(series))
    
    return {
        'statusCode': 200,
        'body': json.dumps('Dados salvos com sucesso no S3!')
    }
