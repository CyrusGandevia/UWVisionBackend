"""
Django settings for UWVision project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import requests

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

ENV = os.environ.get(
    'ENV',
    'test'
)

if ENV == 'production':
    SECRET_KEY = os.environ['SECRET_KEY']
    DEBUG = False
    ALLOWED_HOSTS = [
        'uwvision-backend.com',
        'www.uwvision-backend.com',
        'UWVision-test.us-east-1.elasticbeanstalk.com',
    ]
    CORS_ORIGIN_WHITELIST = [
        'https://www.uwvision.ca',
        'https://uwvision.ca',
        'https://uwvision.herokuapp.com',
    ]
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True

    # Fix to AWS EB Healthcheck's 400 errors by dynamically adding EC2 IP to allowed hosts
    EC2_INSTANCE_IP = None
    for i in range(10): # Allow 10 retries
        try:
            IMDS_V2_TOKEN = requests.put(
                'http://169.254.169.254/latest/api/token', 
                timeout=0.01,
                headers={'X-aws-ec2-metadata-token-ttl-seconds': '3600'}
            ).text
            EC2_INSTANCE_IP = requests.get(
                'http://169.254.169.254/latest/meta-data/local-ipv4', 
                timeout=0.01,
                headers={'X-aws-ec2-metadata-token': IMDS_V2_TOKEN}
            ).text
        except requests.exceptions.ConnectionError:
            pass
        else:
            break
    
    if EC2_INSTANCE_IP:
        ALLOWED_HOSTS.append(EC2_INSTANCE_IP)

else:
    SECRET_KEY = 'django-insecure-v_-6gliqst5ir*y@rgzb1(brqs-5yly@n1q@owi7e*u0cq%vjp'
    DEBUG = True 
    ALLOWED_HOSTS = [
        "127.0.0.1",
    ]
    CORS_ORIGIN_WHITELIST = (
        'http://localhost:3000',
    )

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# Production Database
if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
# Local Database
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework', # Django REST Framework
    'rest_framework.authtoken', # For Token-based auth
    'corsheaders', # Allows for HTTPS requests from frontend server
    'user',
    'company',
    'job',
    'salary',
    'review',
    'interview_question'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

AUTH_USER_MODEL = "user.User"
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES':(
        'rest_framework.permissions.IsAuthenticated',
    ),
}

ROOT_URLCONF = 'UWVision.urls'

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

WSGI_APPLICATION = 'UWVision.wsgi.application'

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
