from base import *


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../../db.sqlite3'),
    }
}


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'secret key goes here'