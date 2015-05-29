from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager
# Create your models here.

class Users(AbstractBaseUser):
    name        = models.CharField(max_length=50, null=True, blank=True)
    lastname    = models.CharField(max_length=100, null=True, blank=True)
    username    = models.CharField(max_length=100, unique=True)
    #password    = models.CharField(max_length=256)
    email       = models.EmailField()
    phone       = models.CharField(max_length=16, null=True, blank=True)
    corporate   = models.CharField(max_length=128, null=True, blank=True)
    id_number   = models.CharField(max_length=32, null=True, blank=True)
    address     = models.CharField(max_length=256, null=True, blank=True)
    sector      = models.CharField(max_length=128, null=True, blank=True)
    validate    = models.BooleanField(default=False)
    hash_code   = models.CharField(max_length=128, null=True, blank=True)
    
    CLIENT = 1
    ADMIN  = 2
    ROLES_CHOICES = (
        (CLIENT, 'USUARIO'),
        (ADMIN, 'ADMINISTRADOR'),
    )
    rol     = models.IntegerField(choices=ROLES_CHOICES, default=1)
    created = models.DateTimeField(auto_now_add=True)
    
    objects = UserManager()
    USERNAME_FIELD = 'username'

    def set_validate(self):
        self.validate = True
        self.hash_code = ""

    class Meta:
        ordering = ('created',)

class Projects(models.Model):
    SOFTWARE     = 1
    AI           = 2
    ROBOTIC      = 3
    HARDWARE     = 4
    BIOTECHNOLOGY = 5
    AUTOMATIC    = 6
    CATEGORIES_CHOICES = (
        (SOFTWARE, 'Software'),
        (AI, 'AI'),
        (ROBOTIC, 'Robotic'),
        (HARDWARE, 'Hardware'),
        (BIOTECHNOLOGY, 'Bio technology'),
        (AUTOMATIC, 'Automatic systems'),
    )
    name = models.CharField(max_length=128)
    tiny_description = models.CharField(max_length=300)
    description = models.CharField(max_length=500)
    motivation = models.CharField(max_length=500)
    owner = models.ForeignKey('tecnocrowd_backend.Users')
    category = models.IntegerField(choices=CATEGORIES_CHOICES)
    amount_project = models.FloatField()
    valoration = models.FloatField()
    init_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass
        ordering = ('created',)

class Images(models.Model):
    size      = models.IntegerField() 
    caption   = models.CharField(max_length=256)
    image_url = models.FileField(upload_to='static/images/')
    project   = models.ForeignKey('tecnocrowd_backend.Projects')
    created   = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('created',)

class Items_budget(models.Model):
    name_item   = models.CharField(max_length=128)
    amount_item = models.FloatField()
    position = models.IntegerField()

    class Meta:
        ordering = ('position',)

class Collaborations(models.Model):
    date_collaborate = models.DateField(auto_now_add=True)
    amount = models.FloatField()
    comment = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
