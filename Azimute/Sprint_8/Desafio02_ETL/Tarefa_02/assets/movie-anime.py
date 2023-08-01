import requests

url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&sort_by=popularity.desc&with_keywords=285442"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYjgwMjA3ODgxYmYwNGNjYjlhMzI1OGMxZjEyODFlMSIsInN1YiI6IjY0NTNmNTRmODdhMjdhMDE1NDMyNWM2MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.9tYrFHogchw7N6x09PQ4zJTeTz8wGKOqn5dy6LYVQgw"
}

response = requests.get(url, headers=headers)

print(response.text)