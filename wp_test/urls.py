
from django.conf.urls import include, url
from django.contrib import admin
from api.urls import api_urls


urlpatterns = [
    # Admin
    url(r'^admin/', include(admin.site.urls)),

    # REST API
    url(r'^api/', include(api_urls)),
]

