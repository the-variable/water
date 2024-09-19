# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

from celery.schedules import crontab
from datetime import timedelta

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drinko.settings')

# Create a Celery instance and configure it with your Django settings.
app = Celery('drinko')
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Kolkata')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')


#CELERY SETTINGS
app.conf.beat_schedule = {
    'send-mail-hourly': {
        'task': 'sender.views.send',
        'schedule': crontab(minute=0, hour='9-23')
    },
    'send-email-midnight-to-2am': {
        'task': 'sender.views.send',
        'schedule': crontab(minute=0, hour='0-2')
    },
}

# Auto-discover tasks in all installed apps.
app.autodiscover_tasks()
