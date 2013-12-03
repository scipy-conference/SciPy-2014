import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scipy2014.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
