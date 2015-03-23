from django.contrib.auth.models import User, Group
from models import Project, Gallery, Image
from rest_framework import viewsets
from serializers import ProjectSerializer, GallerySerializer, ImageSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class GalleryViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to be viewed or edited.
    """
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
