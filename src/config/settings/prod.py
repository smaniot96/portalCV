from .base import *
import os

DEBUG = False
ALLOWED_HOSTS = ['mydomain.com']

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")