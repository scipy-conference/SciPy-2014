# -*- coding: utf-8 -*-
from . import secrets

DEBUG = False
TEMPLATE_DEBUG = False

# tells Pinax to serve media through the staticfiles app.
SERVE_MEDIA = False

EMAIL_USE_TLS = True
EMAIL_HOST = secrets.email_host
EMAIL_HOST_USER = secrets.email_host_user
EMAIL_HOST_PASSWORD = secrets.email_host_password
EMAIL_PORT = secrets.email_port

STATIC_ROOT = '/home/scipy/site/site_media/'
MEDIA_ROOT = '/home/scipy/site/site_media/media/'

INTERNAL_IPS = [
    "127.0.0.1",
]

ADMINS = [
    ("Sheila", "scipy@codersquid.com"),
]

MANAGERS = ADMINS

DATABASES = {"default": secrets.rackspace_db_config}

# Make this unique, and don't share it with anybody.
SECRET_KEY = secrets.secret_key


FILE_UPLOAD_PERMISSIONS = 0640

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(levelname)s %(message)s"
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple"
        }
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
    "loggers": {
        "django.request": {
            "propagate": True,
        },
    }
}

FILE_UPLOAD_PERMISSIONS = 0644
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')
