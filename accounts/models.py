from django.db import models
from django.contrib.auth.models import PermissionsMixin 
from django.conf import settings
from datetime import datetime
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Group

# User = get_user_model() 
User = settings.AUTH_USER_MODEL

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email,first_name, last_name,password,is_superuser=False, is_active = True, is_staff = False, is_admin= False):
        if not email:
            raise ValueError("An email address is required")

        if not password:
            raise ValueError('Kindly put a password')

        user_obj = self.model(
        
            email = self.normalize_email(email),
            password = password,
            first_name = first_name,
            last_name = last_name,
            
            
            

        )
        user_obj.set_password(password)
        
        user_obj.staff = is_staff
        user_obj.superuser = is_superuser
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password = password,
            is_staff = True
        )
        return user

    def create_superuser(self,email,first_name=None,last_name=None, password=None):
        user = self.create_user (
            email,
            first_name,
            last_name,
            password = password,
            is_staff = True,
            is_superuser = True,
            is_admin = True)
        user.save(using=self._db)      
        return user

        
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=200, unique=True,blank=True, null=True)
    # Landlord = models.BooleanField(default=False)
    # tenant = models.BooleanField(default=False)
    # full_name = models.CharField(max_length=200, null = False, blank=False)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    date_joined = models.DateTimeField(default=datetime.now, blank = True)
    admin = models.BooleanField(default = False)
    staff = models.BooleanField(default=False)
    active = models.BooleanField(default =  True)
    is_superuser =  models.BooleanField(default = False)

    # class Meta:
    #     abstract = True
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    # @property
    # def is_superuser(self):
    #     return self.is_superuser

# class Profile(User):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='user_user')
#     parent_link = models.OneToOneField(User, primary_key = True, parent_link = True, on_delete=models.CASCADE)

class Landlord(User):
    user = models.OneToOneField(User, related_name='Landlord',parent_link=True, on_delete= models.CASCADE)
    # email = models.ForeignKey('self', on_delete = models.DO_NOTHING)
    phone = models.CharField(max_length=200,blank = True, null = True)
    whatsapp = models.CharField(max_length=200)
    photo_landlord = models.ImageField(upload_to='photos/%Y/%m/&d', null=True, blank=True)
    
    def __str__(self):
        return self.first_name


class Tenant(User):
    user = models.OneToOneField(User, parent_link = True,related_name='Tenant', on_delete=models.CASCADE)
    photo_tenant = models.ImageField(upload_to='photos/%Y/%m/&d', blank = True)

    def __str__(self):
        return self.first_name

    
