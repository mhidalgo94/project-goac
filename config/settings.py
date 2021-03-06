"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
from .db import MYSQL, SQLITE
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$$y6^tgfn_ho(u%#890+-(8+uf*zu+m@*_c+#c9wq(o(91j8a^'


ALLOWED_HOSTS = ['*']#['django', '127.0.0.1', 'locahost']

# Application definition
BASE_APP = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
MIS_APP = [
    # usuarios
    'core.usuarios',
    # web
    'core.web',
    # Panel Administracion
    'core.panel',
    # Login
    'core.login',
    # Miembros
    'core.miembros',
    # Talleres
    'core.talleres',
    # Servicios Actino
    'core.servicios.actino',
    # Servicios Pyra y Par
    'core.servicios.pyra_par',
    # Servicios SEOC
    'core.servicios.seoc',
    # Servicios Met
    'core.servicios.met'
]
APP_TERCEROS = [
    # ckeditor post
    'ckeditor',
    'ckeditor_uploader',
    # API REST
    'rest_framework',
    # Limpiar Archivos Media Viejos
    'django_cleanup.apps.CleanupConfig',
    # Doc API swagger
    'drf_yasg',
]


INSTALLED_APPS = BASE_APP + MIS_APP + APP_TERCEROS

CKEDITOR_UPLOAD_PATH = 'uploads/'
KEDITOR_ALLOW_NONIMAGE_FILES = False
CKEDITOR_IMAGE_BACKEND = "pillow" 
CKEDITOR_REQUIRE_STAFF=False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'crum.CurrentRequestUserMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = SQLITE

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

DEFAULT_AUTO_FIELD='django.db.models.AutoField'

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Havana'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]


# Media Files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# login
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboart/'

# Logout
LOGOUT_REDIRECT_URL = '/login/'

# Usuarios
AUTH_USER_MODEL = 'usuarios.Usuarios'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
        'height': 500,
    }
}


# Control Servicios
SERVICE_CONTROL_PATH = os.path.join(BASE_DIR,'static/servicios')
SERVICE_CONTROL_FILE = 'servicios_control.txt'

# Datos Actino
ACTINO_ROOT = os.path.join(BASE_DIR, 'static/servicios/actino/csv')
ACTINO_ESTACIONES = ["D","F", "J", "T"]
ACTINO_HISTORICOS_ROOT = os.path.join(BASE_DIR,'static/servicios/actino/actino_historicos')

# Carpeta de LOG
FOLDER_LOG_ROOT = os.path.join(BASE_DIR,'static/servicios/log')

# Archivo Error Servicios Actino
LOG_ERROR_ACTINO = os.path.join(FOLDER_LOG_ROOT,'actino_log.txt')

# Archivo Error Servicio SEOC
LOG_ERROR_SEOC = os.path.join(FOLDER_LOG_ROOT, 'seoc_log.txt')

# Archivo Error MEt
LOG_ERROR_MET = os.path.join(FOLDER_LOG_ROOT, 'met_log.txt')

# Configuracion Rest Framework
REST_FRAMEWORK = {
    'NON_FIELD_ERRORS_KEY':'errors'
}


# Envio de correo
# EMAIL_HOST = 'smtp.googlemail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'marito.hidalgo94@gmail.com'
# EMAIL_HOST_PASSWORD = '*'
# EMAIL_USE_TLS = True
