from django.db import models
from django.utils.translation import ugettext_lazy as _

class Website(models.Model):
    url = models.URLField(null=False, max_length=200, unique=True, verbose_name=_('url'))
    delay = models.IntegerField(null=False, verbose_name=_('delay'))
    response_code = models.IntegerField(null=True, blank=True, verbose_name=_('response code'))
    response_time = models.CharField(null=True, blank=True, max_length=100, verbose_name=_('response time'))

    def __unicode__(self):
        return self.url