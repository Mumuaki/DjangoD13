import os
from celery import Celery
from django.conf import settings



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoD3.settings')

app = Celery('DjangoD3')
app.config_from_object('django.conf:settings', namespace='CELERY')
# app.conf.broker_connection_retry_on_startup = True
# app.autodiscover_tasks()
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


app.conf.beat_schedule = {
    'print_every_5_seconds': {
        'task': 'simpleapp.tasks.printer',
        'schedule': 5,
        'args': (5,),
    },
}


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
