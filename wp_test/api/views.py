from rest_framework import viewsets, permissions
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope

from django.contrib.auth.models import User, Group
from wp_test.models.website import Website
from wp_test.api.serializers import UserSerializer, GroupSerializer, WebsiteSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class WebsiteViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    #permission_classes = [permissions.IsAdminUser]
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
    filter_fields = ['id', 'url', 'delay', 'response_code', 'response_time']


