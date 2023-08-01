import requests

url = "https://api.themoviedb.org/3/discover/tv?include_null_first_air_dates=false&sort_by=popularity.desc&with_genres=16%252C10759%252C10765&with_keywords=210024%252C13141&with_original_language=ja"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYjgwMjA3ODgxYmYwNGNjYjlhMzI1OGMxZjEyODFlMSIsInN1YiI6IjY0NTNmNTRmODdhMjdhMDE1NDMyNWM2MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.9tYrFHogchw7N6x09PQ4zJTeTz8wGKOqn5dy6LYVQgw"
}

response = requests.get(url, headers=headers)

print(response.text)