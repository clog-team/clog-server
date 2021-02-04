# Movie-it Server

## Running the server locally
1. Clone this repository.
```terminal
$ git clone https://github.com/movie-it/movieit-server.git
```
2. Add `credentials.json`.

:bulb: for team members, check out the team slack channel.
```json
{
  "SECRET_KEY": "PROJECT_SECRET_KEY",
  "MOVIE_API_KEY": "MOVIE_API_KEY",
  "MOVIE_DETAIL_API_KEY": "MOVIE_DETAIL_API_KEY"
}
```
3. Create and activate the virtual environment.
```terminal
$ pip install pipenv
$ pipenv shell
```
4. Install the requirements.
```terminal
$ pip install -r requirements.txt
```
5. Create the database.
```terminal
$ python manage.py migrate
```
6. Run the development server.
```terminal
$ python manage.py runserver
```

The project will be available at **localhost:8000/**
