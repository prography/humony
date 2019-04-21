from config.util import get_server_info_value
import os
import pymysql
pymysql.install_as_MySQLdb()


DEBUG = False
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# APPEND_SLASH=False
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = False

if DEBUG is True:
    SECRET_KEY = "buq*!eias((abkx11b6ab964cs7-at1gw%k^!oypi^1357f6@"
    ALLOWED_HOSTS = [
        "127.0.0.1", "*",
    ]
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

else:
    SETTING_PRD_DIC = get_server_info_value("deployment")
    SECRET_KEY = SETTING_PRD_DIC["SECRET_KEY"]
    DATABASES = {
        'default': SETTING_PRD_DIC['DATABASES']["default"]
    }
    AWS_ACCESS_KEY_ID = SETTING_PRD_DIC["AWS_ACCESS_KEY_ID"]
    AWS_SECRET_ACCESS_KEY = SETTING_PRD_DIC["AWS_SECRET_ACCESS_KEY"]
    AWS_REGION = SETTING_PRD_DIC["AWS_REGION"]
    AWS_STORAGE_BUCKET_NAME = SETTING_PRD_DIC["AWS_STORAGE_BUCKET_NAME"]
    AWS_S3_CUSTOM_DOMAIN = SETTING_PRD_DIC["AWS_S3_CUSTOM_DOMAIN"]
    AWS_S3_OBJECT_PARAMETERS = SETTING_PRD_DIC["AWS_S3_OBJECT_PARAMETERS"]
    AWS_DEFAULT_ACL = SETTING_PRD_DIC["AWS_DEFAULT_ACL"]
    AWS_LOCATION = SETTING_PRD_DIC["AWS_LOCATION"]

    STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR,'static')
    ]
    DEFAULT_FILE_STORAGE = 'config.asset_storage.MediaStorage'
    ALLOWED_HOSTS = [
        "127.0.0.1",
        '.compute.amazonaws.com'
    ]


# AUTH_USER_MODEL = 'account.User'
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'social_core',
    'corsheaders',
    'picxi',
    # 'account',

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'



# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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

# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True



REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.AllowAny',
    # ],
    # #  'DEFAULT_PERMISSION_CLASSES': (
    # #      'rest_framework.permissions.IsAuthenticated',
    # # ),
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #   #  'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    #     'rest_framework.authentication.SessionAuthentication',
    #     'rest_framework.authentication.BasicAuthentication',
    # ),
    # 'DEFAULT_PAGINATION_CLASS':
    # 'rest_framework.pagination.LimitOffsetPagination',
    # 'PAGE_SIZE': 10,
}


AUTHENTICATION_BACKENDS = [
    #'social_core.backends.google.GoogleOAuth2', # Google
    #'social_core.backends.facebook.FacebookOAuth2', # Facebook
    'django.contrib.auth.backends.ModelBackend', # Django 기본 유저모델
]
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

# REST_AUTH_SERIALIZERS = {
#     'USER_DETAILS_SERIALIZER': 'user.serializers.UserDetailsSerializer',
# }

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
