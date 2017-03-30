import logging
import re

from django.core.management.base import BaseCommand
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

import yaml
import requests
import json
import time

from wp_test.models.website import Website

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Updates model website'

    def handle(self, *args, **options):
        for website in Website.objects.all():
            start = time.time()
            r = requests.get(website)
            end = time.time()
            response_code = r.status_code
            response_time = end - start
            self.update_website(website, response_code, response_time)

    def update_website(self, website, response_code, response_time):
        website = Website.objects.get(url=website)
        website.response_code = response_code
        website.response_time = response_time
        website.save()