import boto3
from datetime import datetime

s3 = boto3.resource('s3', aws_access_key_id='AKIATD45Q5FL5I7QSPDS', aws_secret_access_key='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')
bucket_name = 'data-lake-do-fabricio'
raw_prefix = 'Raw/Local/CSV'

now = datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")

movies_file = 'movies.csv'
series_file = 'series.csv'

movies_path = f'{raw_prefix}/Movies/{year}/{month}/{day}/{movies_file}'
series_path = f'{raw_prefix}/Series/{year}/{month}/{day}/{series_file}'

bucket = s3.Bucket(bucket_name)
bucket.upload_file(f'assets/{movies_file}', movies_path)
bucket.upload_file(f'assets/{series_file}', series_path)
