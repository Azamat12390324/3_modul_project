from pathlib import Path
import os
from .jazzmin_config import *
from django.utils.translation import gettext_lazy as _


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-+8ukdm-grg9)%@0(bvh*or0^3=yok^9#065(_urr7lqeb^b^4w'

DEBUG = True

ALLOWED_HOSTS = []


DJANGO_APPS = [
     'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

CUSTOM_APPS = [
    'home_1',
    'home_2',
    'shop_layouts',
    'other_pages',
    'product_types',
    
    
]



INSTALLED_APPS = DJANGO_APPS + CUSTOM_APPS 

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware'
]

ROOT_URLCONF = 'core.urls'

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True

LANGUAGES = (
    ("uz", "Uzbek"),
    ("ru", "Russian"),
    ("en", "English"),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'

LOCALE_PATHS = BASE_DIR / 'locale',



STATIC_URL = 'static/'
STATICFILES_DIRS = [
   os.path.join(BASE_DIR / 'static'),
]    


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR / 'media')


#CKEDITOR
#CKEDITOR_UPLOAD_PATH = "ckeditor/contents"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
