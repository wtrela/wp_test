from __future__ import absolute_import, unicode_literals
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
from django.core.management import call_command
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

app = Celery('wp_test')

app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@app.task
def load_yaml():
    logger.info("task")
    call_command('load_yaml')


@app.task
def request_website():
    logger.info("task")
    call_command('request_website')


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):

    # start async call here each time celery is initialized
    load_yaml.delay()
    request_website.delay()

    # periodical calls
    sender.add_periodic_task(crontab(second='*/75'), request_website)


