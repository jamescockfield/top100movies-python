from django.conf import settings
from typing import cast

class ApplicationSettings():
    TMDB_API_URL: str
    TMDB_ACCESS_TOKEN: str

application_settings = cast(ApplicationSettings, settings)
