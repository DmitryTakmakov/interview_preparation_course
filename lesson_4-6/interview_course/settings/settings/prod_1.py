import os

from .base import *

SITE_ID = 1
DEBUG = False
ALLOWED_HOSTS = ['*']
SECRET_KEY = os.environ['SECRET_KEY']
