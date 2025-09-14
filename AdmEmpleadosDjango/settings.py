"""
Django settings for AdmEmpleadosDjango project.
"""

from pathlib import Path
import os

# ===============================
# BASE_DIR
# ===============================
BASE_DIR = Path(__file__).resolve().parent.parent

# ===============================
# TEMPLATE_DIR
# ===============================


# ===============================
# SECURITY
# ===============================
SECRET_KEY = 'django-insecure-f3qr5m!jwcp)*y@9kj=x@#w%qwjpck90lk@@m_@$&#18bk7rm2'
DEBUG = True
ALLOWED_HOSTS = []

# ===============================
# APPLICATIONS
# ===============================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'moduloEmpleados',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'AdmEmpleadosDjango.urls'

# ===============================
# TEMPLATES
# ===============================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'AdmEmpleadosDjango.wsgi.application'

# ===============================
# DATABASE (MySQL / MariaDB)
# ===============================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rrhh1',
        'USER': 'root',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# ===============================
# PASSWORD VALIDATION
# ===============================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# ===============================
# INTERNATIONALIZATION
# ===============================
LANGUAGE_CODE = 'es'   # español
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ===============================
# STATIC FILES
# ===============================
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# ===============================
# DEFAULT PK FIELD
# ===============================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
