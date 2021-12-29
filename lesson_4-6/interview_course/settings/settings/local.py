from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+n$ljmeacnf6j^e@a9d(__*6mpa3*pn29#$deq5ed#rm0=n@$s'
DEBUG = True
ALLOWED_HOSTS = ['*']

SITE_ID = 1

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_db',
        'USER': 'django',
        'PASSWORD': 'qwerty123',
        'HOST': 'db',
        'PORT': '5432'
    }
}
