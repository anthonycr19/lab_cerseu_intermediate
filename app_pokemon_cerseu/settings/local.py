from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-sj6(43p6(g=$zn1ws1+a5-_l9)cjm$9h)7%wv62+&@1dv9%+iu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_pokemon_owner',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',   # '127.0.0.1'
        'PORT': '5432'
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'



