DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'profcom_test_api',
        'USER': 'django',
        'PASSWORD': 'django_test',
        'HOST': 'db',
        'PORT': '5432',
    }
}

CORS_ALLOW_ALL_ORIGINS: True