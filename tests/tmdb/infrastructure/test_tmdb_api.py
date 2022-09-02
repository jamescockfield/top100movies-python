from unittest.mock import patch, Mock
from django.test import SimpleTestCase

from tmdb.infrastructure.tmdb_api import TmdbApi
from tmdb.application.application_settings import application_settings

@patch('requests.get')
class TmdbApiTests(SimpleTestCase):
    api = TmdbApi(application_settings)

    base_url = application_settings.TMDB_API_URL
    movie_id = '69420'
    url = f'{base_url}/movie/{movie_id}'

    def test_gets_auth_header(self, mock_get: Mock) -> None:
        headers = { 'Authorization': 'accessToken' }

        self.api.get_movie(self.movie_id)

        mock_get.assert_called_with(self.url, headers = headers)

    def test_gets_movie(self, mock_get: Mock) -> None:
        expected_movie_data = { 'movie': 'data' }

        mock_get.return_value.json.return_value = expected_movie_data

        movie_data = self.api.get_movie(self.movie_id)

        self.assertEqual(movie_data, expected_movie_data)
