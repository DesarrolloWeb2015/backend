# from django.contrib.auth.models import User, Group
from clients.models import Clients
from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = ('created', 'username', 'email', 'password')


