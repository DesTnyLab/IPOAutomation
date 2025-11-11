from .base import *


DEBUG = True


import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('PG_HOST', 'postgres'),  # Use 'postgres-db' here
        'PORT': os.getenv('PG_PORT', 5432),
    }
}


