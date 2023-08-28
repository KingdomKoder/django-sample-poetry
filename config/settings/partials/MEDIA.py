# check local and production settings

import os

from .BASE import ROOT_DIR, CONFIG_DIR

MEDIA_URL = '/media/'
MEDIA_ROOT = str(ROOT_DIR('mediafiles'))
