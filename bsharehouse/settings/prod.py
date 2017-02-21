from bsharehouse.settings.common import *

DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Link the S3 instance
INSTALLED_APPS += ('storages',)
AWS_STORAGE_BUCKET_NAME = "bsharehouses3"
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = S3_URL

# Link the Postgres DB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bsharehousedb',
        'USER' : 'bsharehouse',
        'PASSWORD' : r"M*%zSzz79C!2",
        'HOST' : 'bsharehousedb.convlvgvotec.us-west-2.rds.amazonaws.com',
        'PORT' : '5432',
    }
}
