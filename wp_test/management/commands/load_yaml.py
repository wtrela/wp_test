import logging
from django.core.management.base import BaseCommand

import yaml

from wp_test.models.website import Website

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Load yml file and creates models'

    def handle(self, *args, **options):
        with open('config.yml', 'r') as stream:
            yml = yaml.safe_load(stream)

        print yml
        for key, value in yml.iteritems():
            for entry in value:
                self.update_website(entry['url'], entry['delay'])

    def update_website(self, url, delay):
        print url, delay
        Website.objects.update_or_create(
            url=url,
            delay=delay
        )
