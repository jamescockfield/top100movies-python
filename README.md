## MyTop100Movies - API,Database,CRUD

Application which lets users set their top 100 movies. Movies could come from an API like The Movie Database (http://tmdb.org). 
Should allow for users to add a movie, list and rank their movie selections. Start with basic CRUD for movies and add features.

### Running

1. Copy `.env.example` to `.env` and set variables
2. Run `pipenv python manage.py migrate`
3. Run `pipenv python manage.py runserver`
4. Endpoints can be pinged from `localhost:8000`

### Planned features

- The Movie Database (http://tmdb.org) API integration

- Database layers

- User authentication

- Autocomplete search bar
