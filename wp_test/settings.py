import os

####################
# Application meta #
####################

PROJECT_PATH = os.environ.get('PROJECT_PATH')
PACKAGE_PATH = os.environ.get('PACKAGE_PATH')

SECRET_KEY = os.environ.get('SECRET_KEY')

##########################
# Application definition #
##########################

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'rest_framework',
    'crispy_forms',
    'oauth2_provider',
    'corsheaders',
    'wp_test',
]

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
    'corsheaders.middleware.CorsMiddleware',
)
CORS_ORIGIN_ALLOW_ALL = True

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'}
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.BasicAuthentication',
            'oauth2_provider.ext.rest_framework.OAuth2Authentication',
        ),
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.ModelSerializer',
    'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.IsAuthenticated',
        ),
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}

ROOT_URLCONF = 'wp_test.urls'

WSGI_APPLICATION = 'wp_test.wsgi.application'

############
# Database #
############

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    },
}

#################
# Globalization #
#################

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('en', 'English'),
)

LOCALE_PATHS = (
    os.path.join(PACKAGE_PATH, 'locale'),
)

DATETIME_FORMAT = 'Y-m-d H:i:s'

DATE_FORMAT = 'Y-m-d'

################
# Static files #
################

MEDIA_ROOT = os.path.join(PACKAGE_PATH, 'media')

MEDIA_URL = '/media/'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PACKAGE_PATH, 'static'),
)

#############
# Templates #
#############

TEMPLATES = (
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': (
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.request',
                'django.template.context_processors.tz',

                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ),
            'debug': True,
        }
    },
)
DEBUG = True


###########
# Logging #
###########

import logging.config


LOGGING_CONFIG = None

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] [%(levelname)s] [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%Y/%b/%d %H:%M:%S",
        },
        'simple': {
            'format': '[%(asctime)s] [%(levelname)-7s] [%(name)s] %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'formatter': 'simple',
            'class': 'logging.StreamHandler',
        },
        'file_django': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'formatter': 'verbose',
            'filename': '/app/logs/django.log',
            'class': 'logging.FileHandler',
            'delay': True,
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        'django.security': {
            'handlers': ['console', 'file_django'],
            'propagate': False,
        },
        'wp_test': {
            'handlers': ['console', 'file_django', 'mail_admins'],
            'level': 'DEBUG',
        },
        'py.warnings': {
            'handlers': ['console'],
        },
    }
}

logging.config.dictConfig(LOGGING)

###########
# Celery #
###########
BROKER_URL = 'redis://redis'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'