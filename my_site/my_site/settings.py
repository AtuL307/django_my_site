"""
Django settings for my_site project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import json
import logging
import logging.handlers

from os import getenv, path, getcwd
from pathlib import Path
from dotenv import load_dotenv # type: ignore
load_dotenv()


##########################  CONFIG  ##########################
CONFIG_PATH = path.join(getcwd(), 'master')
# print("path: ", CONFIG_PATH)
ENVIRONMENT  = getenv('DJANGO_EVN', 'development')

if ENVIRONMENT == 'production':
    CONFIG_FILE_PATH = path.join(CONFIG_PATH, 'config_pro.json')

else:
    CONFIG_FILE_PATH = path.join(CONFIG_PATH, 'config_dev.json')
        
with open(CONFIG_FILE_PATH, 'r') as config_file:
    env_config = json.load(config_file)
    

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = Path.joinpath(BASE_DIR, 'templates')
STATIC_DIR = Path.joinpath(BASE_DIR, 'static')
LOG_FILE = Path.joinpath(BASE_DIR, 'mysite_log')



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env_config['DEBUG']

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_results',
    'django_celery_beat',
    'django_extensions',
    'django_ses',
    
    'rest_framework',
    'whitenoise.runserver_nostatic',
    
    'storages',
    'core',
    'blog',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'my_site.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'my_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

############################## Database Configuration ##############################

# Replace placeholders in the configuration with actual values from the .env file
if ENVIRONMENT == 'production':
    
    env_config['DATABASE']['default']['NAME'] = getenv('AWS_DB_NAME')
    env_config['DATABASE']['default']['USER'] = getenv('AWS_DB_USER')
    env_config['DATABASE']['default']['PASSWORD'] = getenv('AWS_DB_PASSWORD')
    env_config['DATABASE']['default']['HOST'] = getenv('AWS_DB_HOST')
    env_config['DATABASE']['default']['PORT'] = getenv('AWS_DB_PORT')
else:
    env_config['DATABASE']['default']['NAME'] = getenv('DB_NAME')
    env_config['DATABASE']['default']['USER'] = getenv('DB_USER')
    env_config['DATABASE']['default']['PASSWORD'] = getenv('DB_PASSWORD')
    env_config['DATABASE']['default']['PORT'] = getenv('DB_PORT')
    
    
DATABASES = env_config['DATABASE']

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

############################## S3 setting ##############################
if ENVIRONMENT == 'production':
    
    env_config['AWS_S3']['ACCESS_KEY_ID'] = getenv('AWS_ACCESS_KEY_ID')
    env_config['AWS_S3']['SECRET_ACCESS_KEY'] = getenv('AWS_SECRET_ACCESS_KEY')
    custom_bucket = env_config['AWS_S3']['STORAGE_BUCKET_NAME'] = getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_CUSTOM_DOMAIN = env_config['AWS_S3']['S3_CUSTOM_DOMAIN'] = f"{custom_bucket}.s3.amazonaws.com"


# AWS_S3_CONFIG = env_config['AWS_S3']
# print(AWS_S3_CONFIG)
    # AWS_ACCESS_KEY_ID = getenv('AWS_ACCESS_KEY_ID')
    # AWS_SECRET_ACCESS_KEY = getenv('AWS_SECRET_ACCESS_KEY')
    # AWS_STORAGE_BUCKET_NAME = getenv('AWS_STORAGE_BUCKET_NAME')
    # AWS_S3_REGION_NAME = getenv('AWS_S3_REGION_NAME')
    # AWS_S3_SIGNATURE_VERSION = 's3v4'
    # AWS_DEFAULT_ACL = None
    # AWS_S3_FILE_OVERWRITE = False
    # AWS_S3_VERIFY = True
    # AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    # DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

######## s3 static settings ########
# STATIC_LOCATION = 'staticfile'
# STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
# STATICFILES_STORAGE = 'my_site.storage_backends.StaticStorage'

####### s3 public media settings #######
# PUBLIC_MEDIA_LOCATION = 'media'
# MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
# DEFAULT_FILE_STORAGE = 'hello_django.storage_backends.PublicMediaStorage'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_ROOT = Path.joinpath(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
    
#Media Files
MEDIA_ROOT = Path.joinpath(BASE_DIR, 'uploads')
MEDIA_URL = "/posts-media-files/"       
    
STATICFILES_DIR = [STATIC_DIR]
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



############################## Email Configuration  ##############################

if ENVIRONMENT == 'production':
    
    env_config['EMAIL']['ACCESS_KEY_ID'] = getenv('AWS_ACCESS_KEY_ID')
    env_config['EMAIL']['SECRET_ACCESS_KEY'] = getenv('AWS_SECRET_ACCESS_KEY')
    env_config['EMAIL']['REGION_ENDPOINT'] = getenv('AWS_SES_REGION_ENDPOINT')
    env_config['EMAIL']['HOST_USER'] = getenv('EMAIL_HOST_USER')

else:
    env_config['EMAIL']['HOST_USER'] = getenv('EMAIL_HOST_USER')
    env_config['EMAIL']['HOST_PASSWORD'] = getenv('EMAIL_HOST_PASSWORD')
    

EMAIL = env_config["EMAIL"] 


############################## Session Configuration ##############################

# Session engine (default is database-backed sessions)
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# Ensure session cookies are correctly configured
SESSION_COOKIE_NAME = 'sessionid'
SESSION_COOKIE_SECURE = False  # Set to True in production with HTTPS
SESSION_COOKIE_HTTPONLY = True



############################## Celery Configuration ##############################

CELERY_BROKER_URL = "redis://127.0.0.1:6379"
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_EXTENDED = True

CELERY_TIMEZONE = "Asia/Kolkata"
CELERY_RESULT_BACKEND = 'django-db'



#################################### Logging Config ####################################

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters':{
        'standard':{
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
        'simple':{
            'formate': '%(levelname)s - %(message)s',
        }
    }, 
    'handlers': {
        'file':{
            'class': 'logging.handlers.RotatingFileHandler',
            'filename':Path.joinpath(LOG_FILE, 'mysite.log') ,
            'maxBytes': 1024*1024*10,
            'level': 'DEBUG',
            'formatter': 'standard',
            'backupCount': 2
            
        },
        'console':{
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'standard'
            
        },
    },
    
    'loggers':{
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
        'blog':{
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'core':{
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
            
    },
}
