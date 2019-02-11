from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.nepexgroup.tk']
ORGANIZATION_ADMIN = 'nepex.nepexgroup.tk'
AUTH_PASSWORD_VALIDATORS = []

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

INTERNAL_IPS = '127.0.0.1'

# https://stackoverflow.com/questions/26598738/how-to-create-user-database-in-script-for-docker-postgres
DATABASES = {
    'default': {
        'ENGINE': 'tenant_schemas.postgresql_backend',
        'NAME': 'postgres',  # set postgres database by default docker
        'USER': 'postgres',  # set postgres user by default docker
        # 'PASSWORD': 'password',
        'HOST': 'db',  # set in docker-compose.yml
        'PORT': 5432,  # default postgres port
        'ATOMIC_REQUESTS': True,
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',  # For Browsable API
        # 'rest_framework.authentication.TokenAuthentication',  # For Frontend(Token based)
    ),
    # 'DEFAULT_PAGINATION_CLASS': 'dsis.utils.pagination.PageNumberPagination',
    #
    # 'PAGE_SIZE': 10,
    # 'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    # Use Django's standard `django.contrib.autlh` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        # 'rest_framework.permissions.AllowAny'
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    )
}
