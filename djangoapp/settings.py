
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --- Configuração de Segurança e Ambiente ---

# A chave secreta é lida da variável de ambiente `SECRET_KEY`.
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-@e^z-v71g@+6_j85_d=12#m#9v2_#g81%j7$3k2d(2@k7#t_l')

# O modo DEBUG é controlado pela variável de ambiente `DEBUG`.
DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'

# Em modo de desenvolvimento, permita todos os hosts.
ALLOWED_HOSTS = ['*']

# Inicializa a lista de origens confiáveis para CSRF.
CSRF_TRUSTED_ORIGINS = []

# Em modo de desenvolvimento, confia dinamicamente em qualquer subdomínio 
# do cloudworkstations.dev usando a sintaxe de wildcard correta ('.').
if DEBUG:
    # A URL completa do cluster, se disponível, é a mais segura.
    cluster_url = os.environ.get('CLUSTER_URL')
    if cluster_url:
        CSRF_TRUSTED_ORIGINS.append(cluster_url)
    
    # Como fallback, confie em qualquer subdomínio. O '.' inicial é crucial.
    CSRF_TRUSTED_ORIGINS.append('https://.cloudworkstations.dev')
else:
    # Em produção, você deve definir explicitamente seus domínios confiáveis.
    # Ex: CSRF_TRUSTED_ORIGINS = ['https://meudominio.com']
    pass

# --- Fim da Seção de Configuração ---


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # API and Auth
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'dj_rest_auth.registration',

    # django-allauth requirements
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    
    # Our Apps
    'usuario',
    'produtos',
    'carrinho',
    'pedidos',
]

MIDDLEWARE = [
    # Nosso middleware de depuração para inspecionar cabeçalhos
    # 'djangoapp.middleware.HeaderDebugMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware', # Desativado temporariamente para diagnóstico
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware', # Added for django-allauth
]

ROOT_URLCONF = 'djangoapp.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'djangoapp.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media files (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom user model
AUTH_USER_MODEL = 'usuario.User'

# --- AUTHENTICATION SETTINGS ---
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # Needed to login by username in Django admin, regardless of `allauth`
    'allauth.account.auth_backends.AuthenticationBackend', # `allauth` specific authentication methods, such as login by e-mail
)

LOGIN_URL = '/accounts/login/' # Explicitly set the login URL
LOGIN_REDIRECT_URL = '/usuario/profile/'
LOGOUT_REDIRECT_URL = '/'
SITE_ID = 1 # Required for dj-rest-auth and allauth

ACCOUNT_ADAPTER = 'usuario.adapters.MyAccountAdapter'

# REST Framework configuration for JWT authentication
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# Simplified allauth settings for development
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = False
