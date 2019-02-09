from .base import *

DEBUG = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'logfile': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, '..', '..', 'logs', 'debug.log')
        },
    },
    'loggers': {
        'django': {
            'handlers': ['logfile'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}

ALLOWED_HOSTS = ['localhost', 'nerp.awecode.com', 'lumbini.awecode.com', 'sdkm.govnp.site', 'govnp.site']

SERVER_EMAIL = ''

STATIC_ROOT = os.path.join(BASE_DIR, '..', '..', 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, '..', '..', 'media')
MEDIA_URL = '/media/'

INSTALLED_APPS += (
)

MIDDLEWARE += [
]

WEBPACK_ASSETS = {
    "app": {
        "js": "dist/js/app.bundle-4e9d083f6c7a99629cb8.js",
        "css": "dist/css/app-4e9d083f6c7a99629cb8.css"
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, '..', 'db.sqlite3'),
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'tenant_schemas.postgresql_backend',
        'NAME': 'nerp',
        'USER': 'nerp',
        'PASSWORD': 'br3W7l/37gk8CdQ',
        'HOST': 'db',
        'PORT': '',
        'ATOMIC_REQUESTS': True,
    }
}
