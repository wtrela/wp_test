from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from wp_test.api.views import UserViewSet, GroupViewSet, WebsiteViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'websites', WebsiteViewSet)


api_urls = [
    # Rest API
    url(r'^v0/', include([
        url(r'^', include(router.urls)),

        # API authentication
        url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    ]))
]
