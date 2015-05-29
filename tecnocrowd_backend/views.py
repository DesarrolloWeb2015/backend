# Create your views here.
import time
import hashlib
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, Group
from models import Projects, Users, Collaborations, Images, Items_budget
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route, permission_classes
from rest_framework.permissions import AllowAny
from serializer import UserSerializer, GroupSerializer, UsersSerializer, ProjectsSerializer, ImagesSerializer,Items_budgetSerializer, CollaborationsSerializer
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail

class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UsersSerializer
    queryset = Users.objects.all()
    
    def _createHash(self):
        hash = hashlib.sha1()
        hash.update(str(time.time()))
        return hash.hexdigest()[:-10]
    
    def list(self, request):
        queryset = Users.objects.all()
        serializer = UsersSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        hash_code = self._createHash()
        request.DATA['hash_code'] = hash_code
        serializer = UsersSerializer(data=request.DATA)

        if serializer.is_valid():
            self.pre_save(serializer.object)
            self.object = serializer.save(force_insert=True)
            self.post_save(self.object, created=True)
            self.object.save()
            subject, from_email, to = 'validate account', 'tecnocrowd@auth.com', request.DATA['email']
            text_content = "Gracias por registrarte en nuestra plataforma, por favor, valida tu cuenta"
            html_content = '<div>\
                                <img src="http://daw02.aiocs.es/frontend/images/logo5.png" height="100"/>\
                            </div>\
                            <div>\
                                Gracias por registrarte en nuestra plataforma, por favor, valida tu cuenta\
                                haciendo click en el siguiente enlace: \
                                <a href="http://daw02.aiocs.es/frontend/#/validate?c='+hash_code+'">Validar!!</a>\
                            </div>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED,headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @list_route(methods=['get'])
    def validate_account(self, request):
        obj = get_object_or_404(Users, hash_code=request.GET['c'])
        if obj:
            serializer = UsersSerializer(obj)
            if serializer.is_valid:
                obj.set_validate()
                obj.save()
                return Response({'status':'validation complete'})
        return Response({'status': request.GET['c']})

    @list_route(methods=['get'])
    @permission_classes((AllowAny,))
    def login_user(self, request):
        usrLogin = get_object_or_404(Users,username=request.GET['username'], password=request.GET['password'])
        if usrLogin:
            serializer = UsersSerializer(usrLogin)
            return Response(serializer.data)
        return Response({'status':status.HTTP_400_BAD_REQUEST})

class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

    def list(self, request):
        queryset = Users.objects.all()
        serualizer = ProjectsSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        return Response({'status':'only logued users can create projects'})


class ImagesViewSet(viewsets.ModelViewSet):
    serializer_class = ImagesSerializer

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return Images.object.get(project=project_id)
