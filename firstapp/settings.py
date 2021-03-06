"""
Django settings for firstapp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+#=e9l_mlg-iuxf5#0&aibyd#f$7j7we+&p)jtu)$nnjd)y_v-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

TEMPLATE_DIRS = (
<<<<<<< HEAD
    '/home/snapp/djangoenv/bin/firstapp/templates',
    '/home/snapp/djangoenv/bin/firstapp/article/templates',
    '/home/snapp/djangoenv/bin/firstapp/name_blog/templates',
=======
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, 'article', 'templates'),
    os.path.join(BASE_DIR, 'name_blog', 'templates'),
>>>>>>> upstream/master
)


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
<<<<<<< HEAD
    'article',
    'name_blog',
=======
    'foundation',
    'article',
>>>>>>> upstream/master
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'firstapp.urls'

WSGI_APPLICATION = 'firstapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'our_db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

<<<<<<< HEAD
=======
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

>>>>>>> upstream/master
STATIC_URL = '/static/'
