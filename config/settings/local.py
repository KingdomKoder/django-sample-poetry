import os

from .partials import *


DEBUG = True

INSTALLED_APPS += [
    # 'debug_toolbar',
    'django_extensions',
]

INTERNAL_IPS = ['127.0.0.1', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['POSTGRES_NAME'],
        'USER': os.environ["POSTGRES_USER"],
        'PASSWORD': os.environ["POSTGRES_PASSWORD"],
        'HOST': os.environ["POSTGRES_HOST"],
        'PORT': os.environ["POSTGRES_PORT"],
    }
}

# # MEDIA local
# MEDIA_URL = '/media/'
# MEDIA_ROOT = str(ROOT_DIR('mediafiles'))
