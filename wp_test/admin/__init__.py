from django.contrib.admin import site as admin_site
from django.utils.translation import ugettext_lazy as _

from wp_test import models

from wp_test.admin.website import WebsiteAdmin

admin_site.site_title = _('WP Test')
admin_site.site_header = _('WP Test Admin')
admin_site.index_title = _('Admin root')

admin_site.register(models.Website, WebsiteAdmin)
