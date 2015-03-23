from django.contrib.auth.models import User, Group
from models import Clients
from rest_framework import viewsets
from serializers import ClientSerializer


class ClientsViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed or edited.
    """
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer

