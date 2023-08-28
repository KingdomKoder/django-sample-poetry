# Application definition
ADMIN_APPS = [
]
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
]

THIRD_PARTY_APPS = [
]

LOCAL_APPS = [
]

INSTALLED_APPS = ADMIN_APPS + DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
