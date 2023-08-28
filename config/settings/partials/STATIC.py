import os

from .BASE import ROOT_DIR, CONFIG_DIR

STATIC_URL = '/static/'
# before collectstatic
# STATIC_ROOT = str(ROOT_DIR('staticfiles'))
# STATICFILES_DIRS = (
#     str(ROOT_DIR.path('static')),
# )
# after collectstatic
STATIC_ROOT = str(ROOT_DIR('static_files'))
STATICFILES_DIRS = (
    str(ROOT_DIR.path('staticfiles')),
)
