###########################################
#                 WARNING                 #
# Production CI will overwrite this file! #
###########################################

from __future__ import absolute_import, unicode_literals
__version__ = '0.0.0'  # Will be last git TAG on production
__build__ = '000000'  # Will be YYMMDD of deployment date on production


# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

__all__ = ['celery_app']