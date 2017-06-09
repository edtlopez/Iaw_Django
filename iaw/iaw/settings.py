"""
Django settings for iaw project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9z0yt5bh&=l)hhj88g69g7ffnxsp@ex-=l#9b8a5hm1m*or3vi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["www.iawasir2.tk"]


# Application definition

app_name = 'buscador'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'buscador',
    'django_extensions',
    'social_django',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]

#TEMPLATE_DIRS = (
#    os.path.join(PROJECT_PATH,'buscador/templates/buscador'),
#)



ROOT_URLCONF = 'iaw.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'iaw.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': '02520e',
        'HOST': '172.17.0.1',   # Or an IP Address that your DB is hosted on
        'PORT': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

# Cassandra settings

#DATABASES = {
#    'default': {
#        'ENGINE': 'django_cassandra_engine',
#        'NAME': 'db',
#        'TEST_NAME': 'test_db',
#        'HOST': '172.17.0.2',
#        'OPTIONS': {
#            'replication': {
#                'strategy_class': 'SimpleStrategy',
#                'replication_factor': 1
#            }
#        }
#    }
#}

AUTHENTICATION_BACKENDS = (
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GoogleOAuth',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.yahoo.YahooOpenId',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY =  "819629841066-qsu3s0c6rea71marh5450bidofrmkh65.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "e_qTtUc_QjrANsZoA9VzHCHq"


#PATH = '/var/www/iaw'


SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'social_core.pipeline.social_auth.associate_by_email',
)


SOCIAL_AUTH_RAISE_EXCEPTIONS = False
SOCIAL_AUTH_PROCESS_EXCEPTIONS = 'social_auth.utils.log_exceptions_to_messages'


# Configuracion de seguridad

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
