# -*- coding: utf-8 -*-
# Django settings for account project

import os.path
import posixpath

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                            os.pardir))
PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))

LOCALE_PATHS = [
    os.path.join(os.path.dirname(__file__), 'locale')
]

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# tells Pinax to serve media through the staticfiles app.
SERVE_MEDIA = DEBUG

INTERNAL_IPS = [
    "127.0.0.1",
]

ADMINS = [
    # ("Your Name", "your_email@domain.com"),
]

MANAGERS = ADMINS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",  # Add "postgresql_psycopg2", "postgresql", "mysql", "sqlite3" or "oracle".
        "NAME": "dev.db",                        # Or path to database file if using sqlite3.
        "USER": "",                              # Not used with sqlite3.
        "PASSWORD": "",                          # Not used with sqlite3.
        "HOST": "",                              # Set to empty string for localhost. Not used with sqlite3.
        "PORT": "",                              # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "US/Eastern"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGES = (
    ("en", "English"),
    ("pt", "Portuguese"),
    ("es", "Spanish")
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PACKAGE_ROOT, "site_media", "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = "/scipyla2016/site_media/media/"

# Absolute path to the directory that holds static files like app media.
# Example: "/home/media/media.lawrence.com/apps/"
STATIC_ROOT = os.path.join(PACKAGE_ROOT, "site_media", "static")

# URL that handles the static files like app media.
# Example: "http://media.lawrence.com"
STATIC_URL = "/scipyla2016/site_media/static/"

# Additional directories which hold static files
STATICFILES_DIRS = [
    os.path.join(PACKAGE_ROOT, "static"),
]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = posixpath.join(STATIC_URL, "admin/")

# Make this unique, and don't share it with anybody.
SECRET_KEY = "8*br)9@fs!4nzg-imfrsst&oa2udy6z-fqtdk0*e5c1=wn)(t3"

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
]

MIDDLEWARE_CLASSES = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.transaction.TransactionMiddleware",
    "reversion.middleware.RevisionMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "scipyla2016.urls"

TEMPLATE_DIRS = [
    os.path.join(PACKAGE_ROOT, "templates"),
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "account.context_processors.account",
    "pinax_theme_bootstrap.context_processors.theme",
    "symposion.reviews.context_processors.reviews",
    'scipyla2016.template_utils.sponsors',
]

INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",

    # theme
    "pinax_theme_bootstrap",
    "django_forms_bootstrap",

    # external
    "debug_toolbar",
    "mailer",
    "timezones",
    "metron",
    "markitup",
    "taggit",
    "reversion",
    "easy_thumbnails",
    "sitetree",
    "account",
    "django_extensions",


    # symposion
    "symposion",
    "symposion.sponsorship",
    "symposion.conference",
    "symposion.cms",
    "symposion.boxes",
    "symposion.proposals",
    "symposion.speakers",
    "symposion.teams",
    "symposion.reviews",
    "symposion.schedule",

    # project
    "scipyla2016.proposals",
    "scipyla2016.schedule",
]

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

EMAIL_BACKEND = "mailer.backend.DbBackend"

ACCOUNT_OPEN_SIGNUP = True
ACCOUNT_USE_OPENID = False
ACCOUNT_REQUIRED_EMAIL = False
ACCOUNT_EMAIL_VERIFICATION = False
ACCOUNT_EMAIL_AUTHENTICATION = False
ACCOUNT_UNIQUE_EMAIL = EMAIL_CONFIRMATION_UNIQUE_EMAIL = False

ACCOUNT_SIGNUP_REDIRECT_URL = "dashboard"
ACCOUNT_LOGIN_REDIRECT_URL = "dashboard"
ACCOUNT_LOGOUT_REDIRECT_URL = "home"
ACCOUNT_USER_DISPLAY = lambda user: user.email

AUTHENTICATION_BACKENDS = [
    # Permissions Backends
    "symposion.teams.backends.TeamPermissionsBackend",

    # Auth backends
    "account.auth_backends.EmailAuthenticationBackend",
]

LOGIN_URL = "/scipyla2016/account/login/"  # @@@ any way this can be a url name?

EMAIL_CONFIRMATION_DAYS = 2
EMAIL_DEBUG = DEBUG

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}

MARKITUP_FILTER = ("markdown.markdown", {"safe_mode": True})
MARKITUP_SET = "markitup/sets/markdown"
MARKITUP_SKIN = "markitup/skins/simple"

CONFERENCE_ID = 1

SYMPOSION_PAGE_REGEX = r"(([\w-]{1,})(/[\w-]{1,})*)/"

PROPOSAL_FORMS = {
    "tutorial": "scipyla2016.proposals.forms.TutorialProposalForm",
    "talk-poster": "scipyla2016.proposals.forms.TalkPosterProposalForm",
    "bof": "scipyla2016.proposals.forms.BofProposalForm",
    "sprint": "scipyla2016.proposals.forms.SprintProposalForm",
}

# local_settings.py can be used to override environment-specific settings
# like database and email that differ between development and production.
try:
    from local_settings import *
except ImportError:
    pass
