import logging

from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_lazy as _

import requests
import time

from wp_test.models.website import Website

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Updates model website'

    def add_arguments(self, parser):
        parser.add_argument('website', help=_('Request site for given url'))


    def handle(self, *args, **options):
        website = options['website']
        print website

        start = time.time()
        r = requests.get(website)
        end = time.time()
        response_code = r.status_code
        response_time = end - start

        print response_code
        print response_time
        self.update_website(website, response_code, response_time)

    def update_website(self, website, response_code, response_time):
        website = Website.objects.get(url=website)
        website.response_code = response_code
        website.response_time = response_time
        website.save()