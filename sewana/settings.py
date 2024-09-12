"""
Django settings for sewana project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import environ # 환경변수 설정
import dj_database_url # $DATABASE_URL 환경 변수(정의된 경우)에서 데이터베이스 구성 업데이트
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

env = environ.Env() #환경변수와 .env 파일 로딩
environ.Env.read_env()



SECRET_KEY = "django-insecure-trqzdz)j1umdx#8=5qhi)u9!am_z#fm053q$im4izu-s6=8ag+"

""" SECRET_KEY = env('DJANGO_SECRET_KEY', default='+$7(p9&ssydz03c#z)$i*p+&w5$&x62j_ab&7cg*mz$+5j058*')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', default=False)
 """

DEBUG = False

ALLOWED_HOSTS = ['54.180.127.102', '127.0.0.1'] # 별표 표시로 모든 사용자 허용


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "whitenoise.runserver_nostatic", # 정적파일 미들웨어 whitenoise
    
    "rest_framework",
    "rest_framework.authtoken",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    #"allauth.socialaccount.providers.google",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "rest_framework_simplejwt", # djangorestframework-simplejwt
    "rest_framework_simplejwt.token_blacklist",
    "users",
    "django_filters",
    "journal",
    "board",
    "todo",
    "drf_yasg",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware", # 기본제공 보안 미들웨어
    "whitenoise.middleware.WhiteNoiseMiddleware", #django에서 정적 파일 사용 미들웨어
    "corsheaders.middleware.CorsMiddleware", # CORS 백프론트연결
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware", # 일반적인 보안 강화를 위한 미들웨어
    "django.middleware.clickjacking.XFrameOptionsMiddleware", #ClickJacking 방지
    "django.middleware.csrf.CsrfViewMiddleware", #csrf 방지
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "sewana.custom_exception_handler.ExceptionMiddleware", # 직접 작성한 예외처리 미들웨어
]

# 보안 설정
'''
# HTTP Strict Transport Security
# HSTS 헤더를 설정하여 브라우저가 오직 HTTPS를 사용하도록 강제한다.
SECURE_HSTS_SECONDS = 31536000  # HSTS 헤더를 통해 HTTPS를 강제 (1년)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Content Security Policy (CSP)
# 악성 스크립트 로딩 방지를 위해 CSP 설정을 권장합니다.
# django-csp 패키지 사용 가능. 설치 필요.
# SECURE_CONTENT_TYPE_NOSNIFF = True

""" # Clickjacking 방지
X_FRAME_OPTIONS = "DENY" """

# CORS 허용 도메인 설정 - 특정 도메인만 API 요청을 허용한다.
""" CORS_ORICIN_ALLOW_ALL = False
CORS_ALLOWED_ORIGINS = [
    #새로운 도메인을 설정해줘야 한다.
    # "https://example.com",
    # "https://anotherdomain.com",
] """

# CSRF
CSRF_COOKIE_SECURE = True # HTTPS 연결에서만 쿠키가 전송되도록 강제한다.
SECURE_BROWSER_XSS_FILTER = True # 브라우저의 XSS 필터링 기능을 활성화한다.

# SSL/TLS
SECURE_SSL_REDIRECT = True # 모든 HTTP요청을 HTTPS로 강제 리다이렉션한다. 
SESSION_COOKIE_SECURE = True # HTTPS 연결에서만 쿠키가 전송되도록 강제한다.
'''

# 로컬환경 테스트를 위한 설정이다.. 아래를 삭제하고 위의 주석을 해제하자!!
# 프론트엔드에서 자원(resorce)에 잘 접근할 수 있도록 처리해준다.
CORS_ORICIN_ALLOW_ALL = True #모든 도메인에서의 요청을 허용합니다.
CORS_ALLOW_CREDENTIALS = True #요청에 자격 증명을 포함할 수 있도록 허용합니다.

# 여기까지 보안설정

ROOT_URLCONF = "sewana.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "sewana.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
#mdn 문서에서 제공한 코드
if 'DATABASE_URL' in os.environ:
    DATABASES['default'] = dj_database_url.config(
        conn_max_age=500,
        conn_health_checks=True,
    )

""" #db_from_env 변수사용한 코드=>권태형 저 교재에서 제공한 코드
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env) """

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Abstract User로 CustomUser 모델을 생성한 것을 꼭 첫 migrations 전에 적어두어야한다.
AUTH_USER_MODEL = "users.CustomUser"
# Abstract User 모델에 추가한 필드를 Adapter 모듈을 사용하여 추가한다.
ACCOUNT_ADAPTER = 'users.adapter.CustomUserAdapter'
DJ_REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'users.serializers.CustomRegisterSerializer',
}


# 이메일 인증기능 없애기
ACCOUNT_EMAIL_VERIFICATION ='none'
ACCOUNT_EMAIL_VERIFICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
    'EXCEPTION_HANDLER': 'sewana.custom_exception_handler.handle_exception',
}


# JWT 설정 - 시간설정 위하여
from datetime import timedelta

# JWT 설정 - 토큰 접근 수명, 토큰 재활성화 수명, 등
# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": True,
    "ALGORITHM": 'HS256', # JWT 토큰 서명 알고리즘=암호화 알고리즘 정의.
    "SIGNING_KEY": SECRET_KEY, #비밀 키 지정-Django 프로젝트의 비밀키로 설정된다.
    "VERIFYING_KEY": None, # 토큰 서명을 검증할 때 사용하는 공개 키 지정. 비대칭 암호화에서 사용. 기본값은 None이며 대칭 암호화 사용한다는 의미다.
    "AUDIENCE": None, # JWT의 'aud' 클레임을 검증할 때 사용할 값이다.
    "ISSUER": None, # JWT의 'iss'(발급자) Claim을 검증할 때 사용할 값. 기본값은 None이다. 특정 발급자의 토큰을 지정하여, 그것만 신뢰하도록 한다.
    "JWK_URL": None, # JSON Web Key JWK 형식으로 키를 제공하는 URL을 지정한다. 기본값은 None이다. 토큰 검증 시 외부 서비스의 공개 키를 가져오기 위해 사용될 수 있다.
    "LEEWAY": 0, # 토큰의 유효성을 검증할 때 허용되는 시간 차이를 지정. 기본값은 0이다. 서버 간의 시계 차이를 허용하기 위해 토큰 만료 시간에 (초단위의)일정한 시간 차이를 허용할 수 있따.
    "AUTH_HEADER_TYPES": ('Bearer',), # 클라이언트가 인증 헤더에서 사용하는 인증 유형을 지정합니다. 'Bearer'는 JWT 토큰이 "Authorization: Bearer <token>" 형식으로 전송된다는 것을 의미한다.
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION", # 클라이언트가 JWT 토큰을 전달할 때 사용할 헤더 이름을 지정한다. HTTP_AUTHORIZATION은 DJango의 WSGI 인터페이스에 맞춰 설정된 기본값이다. 토큰을 포함한 HTTP 요청 헤더의 이름을 지정한다.
    "USER_ID_FIELD": "id", # JWT 토큰에서 사용할 사용자 ID(식별자)의 필드를 지정한다. Django 모델의 기본 필드인 'id'를 사용한다.
    "USER_ID_CLAIM": "user_id", # JWT 토큰에서 사용자 ID가 저장될 Claim의 이름을 지정한다. "user_id"는 사용자 ID가 JWT 토큰 내에 "user_id"라는 이름의 Claim으로 저장된다는 것을 의미한다.
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    # 사용자를 인증할 때 사용할 규칙을 지정합니다. 여기서는 기본 인증 규칙을 사용하도록 했다.
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    # 사용할 토큰 클래스(들)을 지정합니다.
    "TOKEN_TYPE_CLAIM": "token_type", # JWT 토큰에서 토큰 유형이 저장될 Claim 이름을 지정한다. "token_type" 이라는 이름의 Claim에 토큰의 유형이 저장된다.
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
    # 토큰에서 사용자를 표현할 때 사용할 클래스를 지정합니다. simplejwt에서 제공하는 TokenUser 클래스를 사용한다.
    "JTI_CLAIM": "jti", # JWT 토큰의 'jti' (JWT ID) Claim의 이름을 지정한다. 각 JWT 토큰에 고유한 식별자를 부여하는 Claim이다. 이름을 "jti"라고 지정했다. 
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    # 슬라이딩 토큰의 refrech 만료 시간을 저장할 클레임의 이름을 지정한다. "refresh_exp"라는 이름으로 Claim을 저장한다.
    # 슬라이딩 토큰 : 만료 기간이 갱신되는 토큰
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5), #슬라이딩 토큰의 기본 유효기간 지정
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1), # 슬라이딩 토큰이 처음 발급 된 후 리프레시 가능한 최대 유효기간을 지정.
    
}

""" SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ('Bearer',),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_ROTATION": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": True,
    "ALGORITHM": 'HS256',
    "SIGNING_KEY": SECRET_KEY,
} """

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

if not DEBUG:    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
    STATIC_ROOT = Path(BASE_DIR) / 'staticfiles'
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


""" if not DEBUG:    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
    STATIC_ROOT = Path(BASE_DIR) / 'staticfiles'
    STORAGES = {
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        },
    } """


MEDIA_URL = "media/"
MEDIA_ROOT = Path(BASE_DIR) / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
