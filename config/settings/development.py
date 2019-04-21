import os

from .base import *

SECRET_KEY = "buq*!eias((abkx11b6ab964cs7-at1gw%k^!oypi^1357f6@"
DEBUG = True

INSTALLED_APPS += [
]

ALLOWED_HOSTS = [
    "127.0.0.1", "*",
]

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

MIDDLEWARE += [
]


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
