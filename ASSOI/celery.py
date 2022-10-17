import os
from logging.config import dictConfig

from celery import Celery
from celery.signals import setup_logging
from django.conf import settings

# Configure django settings file considering environment variables.
django_settings_module = os.getenv("DJANGO_SETTINGS_MODULE", "ASSOI.settings")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", django_settings_module)

# Celery configuration settings.
app = Celery("ASSOI")

app.config_from_object('django.conf:settings', namespace='CELERY')


@setup_logging.connect
def config_loggers(*args, **kwargs):  # pragma: no cover
    dictConfig(settings.LOGGING)


# Download all tasks which registered in INSTALLED_APPS
app.autodiscover_tasks()
