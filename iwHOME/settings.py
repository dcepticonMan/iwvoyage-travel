import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-uzm_4#%u4t4#38k9_$a(sx$oq4%64n1q-i1cr2l$=09_a996r4'
DEBUG = True
ALLOWED_HOSTS = [
    'www.iwvoyage.com',
    'iwvoyage.com',
    'webapp-2580515.pythonanywhere.com',
]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'post',
    'destinations',
    'index',
    'service',
    'about',
    'contact',
    'cities',
    'django_ckeditor_5',
    'django_extensions',
    'process',
    'partners',
    'qna',
    'adbanner',
    'booking',
    'deals',
    'mediahub',
    'django.contrib.sitemaps',
]


# CKEditor 5 configurations
CKEDITOR_5_CONFIGS = {
    'default': {
        # Choose the toolbar items you need
        'toolbar': [
            'heading', '|',
            'bold', 'italic', 'underline', 'link', '|',
            'bulletedList', 'numberedList', '|',
            'blockQuote', 'insertTable', '|',
            'undo', 'redo'
        ],
        'height': 300,
        # You can add more CKEditor 5 config options here:
        # https://ckeditor.com/docs/ckeditor5/latest/api/module_core_editor-editorconfig-EditorConfig.html
    }
}



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'iwHOME.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'iwHOME.context_processors.sidebar_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'iwHOME.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'in-v3.mailjet.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = '74c00299648e40e62daa1e47ab7ec63a'
EMAIL_HOST_PASSWORD = '30e6d734f23957870683f79057c81b57'
DEFAULT_FROM_EMAIL = 'luis@iwvoyage.com'
