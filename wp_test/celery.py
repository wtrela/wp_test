from __future__ import absolute_import, unicode_literals
from celery import Celery
from django.conf import settings
from django.core.management import call_command
from celery.utils.log import get_task_logger

from wp_test.models.website import Website

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
def request_website(website):
    logger.info("task")
    logger.info("'request_website', '{}'.format(website)")
    call_command('request_website', '{}'.format(website))


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):

    # start async call here each time celery is initialized
    load_yaml.delay()

    for website in Website.objects.all():
        # periodical calls
        sender.add_periodic_task(website.delay, request_website(website))


