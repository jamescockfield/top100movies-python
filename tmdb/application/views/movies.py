from rest_framework.views import Request, Response, status
from rest_framework import viewsets

from tmdb.application.application_settings import application_settings
from tmdb.infrastructure.tmdb_api import TmdbApi

class MovieViewSet(viewsets.ViewSet):
    tmdb_api = TmdbApi(application_settings)

    def retrieve(self, request: Request):
        movie_id = str(request.query_params.get('movie_id'))

        if not movie_id.isnumeric():
            return Response('movie ID should be an integer', status=status.HTTP_400_BAD_REQUEST)

        movie_data = self.tmdb_api.get_movie(movie_id)

        response = Response(movie_data)

        return response
