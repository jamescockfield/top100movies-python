import os
from dotenv import load_dotenv
from .settings import *

load_dotenv()

TMDB_API_URL = os.getenv('TMDB_API_URL')
TMDB_ACCESS_TOKEN = os.getenv('TMDB_ACCESS_TOKEN')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
