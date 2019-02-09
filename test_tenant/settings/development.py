from .base import *

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

AUTH_PASSWORD_VALIDATORS = []

STATIC_URL = '/static/'

# STATIC_ROOT = os.path.join(BASE_DIR, '..', '..', 'static')
#
# MEDIA_ROOT = os.path.join(BASE_DIR, '..', '..', 'media')
MEDIA_URL = '/media/'

# INSTALLED_APPS += (
#     'debug_toolbar',
#     # 'django_extensions',
# )

# TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = '127.0.0.1'

WEBPACK_ASSET_JSON = os.path.join(BASE_DIR, '../assets.json')

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, '..', 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'tenant_schemas.postgresql_backend',
        'NAME': 'test',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': '',
        'PORT': '',
        'ATOMIC_REQUESTS': True,
    }
}

REST_FRAMEWORK = {
    # 'DEFAULT_PAGINATION_CLASS': 'nerp.utils.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 25,
    # 'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',

    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}
