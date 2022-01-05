from .base import *

DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangoblog',
        'USER': 'root',
        'PASSWORD': '152123',
        'PORT': '3306',
        'HOST': 'localhost',
    }
}


