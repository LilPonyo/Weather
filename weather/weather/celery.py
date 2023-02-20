
# import os
# from celery import *
# from celery.schedules import crontab

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'weather.settings')

# app = Celery('weather')
# app.config_from_object('django.conf:settings', namespace="CELERY")
# app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'every': {
#         'task': 'weather.tasks.repeat_oreder_make',
#         'schedule': crontab(),
#     },
# }