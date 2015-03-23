# from django.contrib.auth.models import User, Group
from projects.models import Project, Gallery, Image
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('created', 'slogan', 'tiny_description', 'description', 'owner')


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image




