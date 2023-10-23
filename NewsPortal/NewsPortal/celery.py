import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPortal.settings')

app = Celery('NewsPortal')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'action_weekly_notifications': {
        'task': 'news.tasks.send_weekly_posts_list',
        'schedule': crontab(minute='00', hour='08', day_of_week='monday'),
    },
}

app.autodiscover_tasks()
