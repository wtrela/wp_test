from __future__ import absolute_import, unicode_literals
from celery import Celery
from django.conf import settings
from django.core.management import call_command
from celery.utils.log import get_task_logger
from twisted.internet import task
from twisted.internet import reactor



logger = get_task_logger(__name__)

app = Celery('wp_test')

app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task
def load_yaml():
    logger.info("load_yaml")
    call_command('load_yaml')


@app.task
def request_website():
    from wp_test.models.website import Website
    def call(*args):
        call_command('request_website', website)

    for website in Website.objects.all():
        l = task.LoopingCall(call, website, website.delay)
        l.start(website.delay)

    reactor.run()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):

    # start async call here each time celery is initialized
    load_yaml.delay()
    request_website.delay()



