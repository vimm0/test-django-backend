import os
from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]

SECRET_KEY = 's0!=6i7rzn-vkzrbxs@dwl*a5@15n!$(wp#pk!%h+0gkav)b43'

SHARED_APPS = (
    'tenant_schemas',  # mandatory, should always be before any django app
    'apps.customer',  # you must list the app where your tenant model resides in

    'django.contrib.contenttypes',

    # everything below here is optional
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
)

TENANT_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',

    'rest_framework.authtoken',

    # your tenant-specific apps
    'apps.blog',
    'apps.user',
)

INSTALLED_APPS = [
    'tenant_schemas',
    'apps.customer',

    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # vendors
    'rest_framework',
    'corsheaders',
    'rest_framework.authtoken',
    'crispy_forms',

    # apps
    'apps.blog',
    'apps.user',

]

MIDDLEWARE = [
    'tenant_schemas.middleware.TenantMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

SITE_ID = 1
TENANT_MODEL = 'customer.Client'
AUTH_USER_MODEL = 'user.CustomUser'
ROOT_URLCONF = 'test_tenant.urls'
PUBLIC_SCHEMA_URLCONF = 'test_tenant.urls_public'
DEFAULT_FILE_STORAGE = 'tenant_schemas.storage.TenantFileSystemStorage'  # tenant

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'test_tenant.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',  # For Browsable API
        # 'rest_framework.authentication.TokenAuthentication',  # For Frontend(Token based)
    ),
    # 'DEFAULT_PAGINATION_CLASS': 'dsis.utils.pagination.PageNumberPagination',
    #
    # 'PAGE_SIZE': 10,
    # 'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    # Use Django's standard `django.contrib.auth` permissions,
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

LANGUAGE_CODE = 'en-us'
LANGUAGES = [
    ('ne', _('Nepali')),
    ('en', _('English')),
]

TIME_ZONE = 'Asia/Kathmandu'
USE_I18N = True
USE_L10N = True
USE_TZ = True

CORS_ORIGIN_WHITELIST = (
    'localhost:8080',
)
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'responseType',
)

DATABASE_ROUTERS = (
    'tenant_schemas.routers.TenantSyncRouter',
)
