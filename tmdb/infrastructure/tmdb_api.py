import requests
from tmdb.application.application_settings import ApplicationSettings

class TmdbApi():
    def __init__(self, settings: ApplicationSettings) -> None:
        self.base_url = settings.TMDB_API_URL
        self.access_token = settings.TMDB_ACCESS_TOKEN

    def _get_auth_header(self) -> dict[str, str]:
        return {'Authorization': self.access_token}

    def get_movie(self, movie_id: str) -> dict[str, str]:
        url = f'{self.base_url}/movie/{movie_id}'
        headers = self._get_auth_header()

        response = requests.get(url, headers = headers)
        movie_data = response.json()

        return movie_data

