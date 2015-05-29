from django.contrib.auth.models import User, Group
from models import Projects, Users, Collaborations, Images, Items_budget
from rest_framework import serializers

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        field = ('url', 'name')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('url','username','email','groups')

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('name','lastname','username','password', 'email', 'phone', 'corporate', 'id_number', 'address', 'sector', 'validate', 'hash_code','created')

class ProjectsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Projects
        fields = ('name','tiny_description','description','motivation','owner','amount_project','category','valoration', 'created', 'ini_date', 'end_data')



class ImagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Images
        fields = ('size','caption','image_url', 'project', 'created')

class Items_budgetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Items_budget
        fields = ('name_item','amount_item','position')

class CollaborationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Collaborations
        fields = ('date_collaborate', 'amount', 'comment', 'created')
