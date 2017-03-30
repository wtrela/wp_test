from rest_framework import serializers

from django.contrib.auth.models import User, Group
from wp_test.models.website import Website


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'



class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = ('url', 'delay', 'response_code', 'response_time')


