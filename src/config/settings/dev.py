from .base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")