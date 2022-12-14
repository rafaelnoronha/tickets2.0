"""
Django settings for tickets project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from datetime import timedelta

from decouple import config, Csv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

OTHER_APPS = [
    'rest_framework',
    'django_filters',
    'rest_framework_simplejwt',
    'django_user_agents',
]

MY_APPS = [
    'apps.core',
    'apps.usuario',
    'apps.auditoria',
    'apps.empresa',
]

INSTALLED_APPS = DJANGO_APPS + OTHER_APPS + MY_APPS

DJANGO_MIDDLEWARES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

OTHER_MIDDLEWARES = [
    'django_user_agents.middleware.UserAgentMiddleware',
]

MY_MIDDLEWARES = []

MIDDLEWARE = DJANGO_MIDDLEWARES + OTHER_MIDDLEWARES + MY_MIDDLEWARES

ROOT_URLCONF = 'tickets.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'tickets.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',

        # "ENGINE": config('ENGINE'),
        # "HOST": config('HOST'),
        # "NAME": config('NAME'),
        # "USER": config('USER'),
        # "PASSWORD": config('PASSWORD'),
        # "PORT": config('PORT'),
    }
}


# Usu??rio personalizado
# https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#substituting-a-custom-user-model

AUTH_USER_MODEL = 'usuario.Usuario'


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'apps.usuario.password_validation.MinimumLengthValidatorCustom',
    },
    {
        'NAME': 'apps.usuario.password_validation.ComprimentoMaximoValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Formatos de data aceitos na hora de criar ou altualizar os dados
# https://docs.djangoproject.com/en/4.1/ref/settings/#date-input-formats

DATE_FORMAT = ['%d-%m-%Y'],
DATE_INPUT_FORMATS = ["%d-%m-%Y", "%Y-%m-%d"],


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


APPEND_SLASH = False


# Configura????es do Django Rest Framework
# https://www.django-rest-framework.org/api-guide/settings/

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissions',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
        'apps.usuario.authentication.JWTAuthenticationCustom',
    ],
    # 'DATE_FORMAT': '%d-%m-%Y',
    # 'DATE_INPUT_FORMATS': ["%d-%m-%Y", "%Y-%m-%d"],
}


# Configura????es do Simple JWT
# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(minutes=5),
    'UPDATE_LAST_LOGIN': True,

    'SIGNING_KEY': config('SIGNING_KEY'),

    'USER_ID_FIELD': 'id',
    'USER_AUTHENTICATION_RULE': 'apps.usuario.authentication.regra_padrao_autenticacao_usuario',

    # 'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken', 'apps.usuario.tokens.ValidarTokenAcesso',),
}