# from django.db import models
# from django.conf import settings
# from datetime import datetime
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Landlord = settings.AUTH_USER_MODEL

# # Create your models here.
# class LandlordManager(BaseUserManager):
#     def create_user(self, email,is_active = True,is_superuser=False, is_staff = False, is_admin= False, password=None):
#         if not email:
#             raise ValueError("An email address is required")

#         if not password:
#             raise ValueError('Kindly put a password')

#         user_obj = self.model(
#             self.normalize_email(email)

#         )
#         user_obj.set_password(password)
#         user_obj.staff = is_staff
#         user_obj.superuser = is_superuser
#         user_obj.admin = is_admin
#         user_obj.active = is_active
#         user_obj.save(using=self._db)
#         return user_obj

#     def create_staffuser(self, email, password=None):
#         user = self.create_user(
#             email,
#             password = password,
#             is_staff = True
#         )
#         return user

#     def create_superuser(self, email, password=None):
#         user = self.create_user (
#             email,
#             password = password,
#             is_staff = True,
#             is_admin = True)
#         user.save(using=self._db)      
#         return user

        
# class Landlord(AbstractBaseUser):
#     email = models.EmailField(max_length=200, unique=True)
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     date_joined = models.DateTimeField(default=datetime.now, blank = True)
#     phone = models.IntegerField(blank = False, null = False)
#     whatsapp = models.IntegerField()
#     photo = models.ImageField(upload_to = 'photos/%Y/%m/&d')
#     admin = models.BooleanField(default = False)
#     staff = models.BooleanField(default=False)
#     active = models.BooleanField(default =  True)
#     superuser =  models.BooleanField(default = False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = LandlordManager()

#     def __str__(self):
#         return self.email

#     def get_full_name(self):
#         return self.first_name
    
#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     @property
#     def is_staff(self):
#         return self.staff

#     @property
#     def is_admin(self):
#         return self.admin

#     @property
#     def is_active(self):
#         return self.active

#     @property
#     def is_superuser(self):
#         return self.is_superuser