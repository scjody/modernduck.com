"""
Django settings for quack project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd(p&5f51s3)_@32gwu94^-91%xs*4ku5gbzjr@i4zjxyrewd%2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'quack',
    'tetristats',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'quack.urls'

WSGI_APPLICATION = 'quack.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

if 'QUACK_USE_SQLITE' in os.environ:
    default_db = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR + 'db.sqlite3',
    }
else:
    default_db = {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'mysql.modernduck.com',
        'NAME': 'django_quack',
        'USER': 'django_quack',
        'PASSWORD': os.getenv('QUACK_MYSQL_PASSWORD'),
    }

DATABASES = {
    'default': default_db,
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.dirname(BASE_DIR) + '/public/static/'

TEMPLATE_DIRS = (os.path.dirname(BASE_DIR) + '/quack/templates',)
