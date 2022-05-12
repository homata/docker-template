"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path
from decouple import config
from decouple import Csv

# Load operating system environment variables and then prepare to use them
# import environ
# env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool, default=False)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1', cast=Csv())  # ['127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig',
    'apps.apps.AppsConfig',
    'rest_framework',
    'import_export',
    'rest_framework.authtoken'
]

if DEBUG:
    INSTALLED_APPS += [
        'django_extensions',
        'debug_toolbar',
    ]

# Application definition
AUTH_USER_MODEL = 'users.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',       # Add for Heroku
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
if DEBUG:
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

if DEBUG:
    INTERNAL_IPS = ['127.0.0.1', '0.0.0.0', 'localhost', ]

# REST_FRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        # 'config.authentication.WithoutCSRFValidationSessionAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',  # Django REST frameworkのGUIを非常にする
    ),
}

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
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

WSGI_APPLICATION = 'config.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ja-jp'
# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),  # プロジェクト直下のstaticディレクトリを指定
)
STATICFILES_FINDERS = (
    # settings.STATICFILES_DIRSに設定したディレクトリからファイルを読み込む
    'django.contrib.staticfiles.finders.FileSystemFinder',
    # アプリケーションのstaticディレクトリからファイルを読み込みむ
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# set upload files directory and url path
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# for Heroku Settings
# ------------------------------------------------------------------------------
if DEBUG:
    try:
        from config.local_settings import *
    except ImportError:
        pass
else:
    import django_heroku
    django_heroku.settings(locals())

    # HerokuのPostgresを設定
    import dj_database_url
    db_from_env = dj_database_url.config()
    DATABASES = {
        'default': dj_database_url.config()
    }
    ALLOWED_HOSTS = ['*']

    # HerokuのConfigを読み込み
    django_heroku.settings(locals())

# GeoDjango on Windows
# ------------------------------------------------------------------------------
# GeoDjango on Windows: “Could not find the GDAL library” / “OSError: [WinError 126] The specified module could not be found”
#  https://stackoverflow.com/questions/49139044/geodjango-on-windows-could-not-find-the-gdal-library-oserror-winerror-12/49159195#49159195
import os
if os.name == 'nt':
    import platform
    POSTGRES = config("DJANGO_WINDOWS_POSTGRES", default=r"C:\Program Files\PostgreSQL\13")
    OSGEO4W = config("DJANGO_WINDOWS_OSGEO4W", default=r"C:\OSGeo4W64")
    assert os.path.isdir(OSGEO4W), "Directory does not exist: " + OSGEO4W

    os.environ['OSGEO4W_ROOT'] = OSGEO4W
    os.environ['POSTGRES_ROOT'] = POSTGRES
    os.environ['GDAL_LIBRARY_PATH'] = OSGEO4W + r"\bin"
    os.environ['GEOS_LIBRARY_PATH'] = OSGEO4W + r"\bin"
    os.environ['PATH'] = OSGEO4W + r"\bin;" + POSTGRES + r"\bin;" + os.environ['PATH']

    GDAL_LIBRARY_PATH = config("DJANGO_GDAL_LIBRARY_PATH", default=r"")