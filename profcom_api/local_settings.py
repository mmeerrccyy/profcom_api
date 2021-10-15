import os

import dj_database_url

DATABASES = {}

DATABASES['default'] = dj_database_url.config(default=os.environ.get("DATABASE_URL"))

CORS_ALLOW_ALL_ORIGINS: True
