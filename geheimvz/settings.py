"""
Django settings for geheimvz project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import environ
import os

import pillow_avif

env = environ.Env(
    ALLOWED_HOSTS=(list, ["localhost", "127.0.0.1"]),
    CACHE_URL=(str, "locmemcache://"),
    CSRF_TRUSTED_ORIGINS=(list, []),
    DATABASE_URL=(str, None),
    DEBUG=(bool, False),
    LANGUAGE_CODE=(str, "de-de"),
    LOG_LEVEL=(str, "WARNING"),
    S3_ACCESS_KEY_ID=(str, None),
    S3_BUCKET_NAME=(str, "django"),
    S3_PUBLIC_URL=(str, None),
    S3_ENDPOINT_URL=(str, None),
    S3_SECRET_ACCESS_KEY=(str, None),
    SECRET_KEY=(
        str,
        "django-insecure-0vmd)dzp1if@fftcsgaka2y5m5+&r#k^!1yq5d3pq8*w)l3ku^",
    ),
    TIME_ZONE=(str, "UTC"),
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = env("ALLOWED_HOSTS")

INTERNAL_IPS = ["127.0.0.1"]

CSRF_TRUSTED_ORIGINS = env("CSRF_TRUSTED_ORIGINS")


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "django_vite",
    "django_components",
    "csp",
    "crispy_forms",
    "crispy_tailwind",
    "django_s3_storage",
    "imagekit",
    "friendship",
    "django_tables2",
    "account.apps.AccountConfig",
    "core.apps.CoreConfig",
    "emoticons.apps.EmoticonsConfig",
    "friends.apps.FriendsConfig",
    "groups.apps.GroupsConfig",
    "invites.apps.InvitesConfig",
    "motd.apps.MotdConfig",
    "pinboard.apps.PinboardConfig",
    "private_messages.apps.PrivateMessagesConfig",
    "search.apps.SearchConfig",
    "debug_toolbar",
    "django_cleanup.apps.CleanupConfig",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "csp.middleware.CSPMiddleware",
]

ROOT_URLCONF = "geheimvz.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "builtins": [
                "django_components.templatetags.component_tags",
            ],
            "loaders": [
                (
                    "django.template.loaders.cached.Loader",
                    [
                        # Default Django loader
                        "django.template.loaders.filesystem.Loader",
                        # Inluding this is the same as APP_DIRS=True
                        "django.template.loaders.app_directories.Loader",
                        # Components loader
                        "django_components.template_loader.Loader",
                    ],
                )
            ],
        },
    },
]

WSGI_APPLICATION = "geheimvz.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": env.db(),
}


# Caches
# https://docs.djangoproject.com/en/5.1/ref/settings/#caches

CACHES = {
    "default": env.cache(),
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = "core.User"

LOGIN_REDIRECT_URL = "index-login"

LOGOUT_REDIRECT_URL = "index"


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = env("LANGUAGE_CODE")

TIME_ZONE = env("TIME_ZONE")

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
# https://github.com/etianen/django-s3-storage
# https://whitenoise.readthedocs.io/en/stable/django.html#add-compression-and-caching-support
# https://github.com/EmilStenstrom/django-components/blob/master/README.md#installation

STATIC_URL = "static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

STORAGES = {
    "default": {
        "BACKEND": "django_s3_storage.storage.S3Storage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

AWS_ACCESS_KEY_ID = env("S3_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("S3_SECRET_ACCESS_KEY")
AWS_S3_BUCKET_NAME = env("S3_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = env("S3_ENDPOINT_URL")
AWS_S3_PUBLIC_URL = env("S3_PUBLIC_URL")

AWS_REGION = "auto"
AWS_S3_BUCKET_AUTH = False

WHITENOISE_ROOT = BASE_DIR / "geheimvz/static"

STATICFILES_FINDERS = [
    # Default finders
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    # Django components
    "django_components.finders.ComponentsFileSystemFinder",
]


# Default primary-200 key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Logging
# https://docs.djangoproject.com/en/5.1/topics/logging/

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": env("LOG_LEVEL"),
            "propagate": False,
        },
    },
}


# Vite Integration
# https://github.com/MrBin99/django-vite

DJANGO_VITE = {
    "default": {
        "dev_mode": DEBUG,
        "static_url_prefix": "core/assets",
    },
}


# Crispy Forms
# https://django-crispy-forms.readthedocs.io/en/latest/
# https://django-crispy-forms.github.io/crispy-tailwind/

CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"

CRISPY_TEMPLATE_PACK = "tailwind"


# Tables
# https://django-tables2.readthedocs.io/en/latest/pages/custom-rendering.html

DJANGO_TABLES2_TABLE_ATTRS = {
    "class": "w-full table-auto",
    "thead": {
        "class": "border-t border-b bg-secondary-200 border-secondary-300 text-secondary-content",
    },
    "tbody": {
        "class": "divide-y divide-primary-300",
    },
    "th": {
        "class": "px-2 py-1 text-left",
    },
    "td": {
        "class": "px-2 py-4 align-top",
    },
}

DJANGO_TABLES2_TEMPLATE = "core/django_tables2/table.html"


# Components
# https://github.com/EmilStenstrom/django-components

COMPONENTS = {
    "dirs": [],
}


# Image Transforms
# https://django-imagekit.readthedocs.io/en/latest/

IMAGEKIT_DEFAULT_CACHEFILE_STRATEGY = "imagekit.cachefiles.strategies.Optimistic"


# Content-Security-Policy
# https://django-csp.readthedocs.io/en/3.8/

CSP_IMG_SRC = ["'self'", "data:"]
if env("S3_PUBLIC_URL"):
    CSP_IMG_SRC.append(env("S3_PUBLIC_URL"))

CSP_REPORT_ONLY = DEBUG
