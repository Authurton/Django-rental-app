# from django.db import models
# from django.conf import settings
# from datetime import datetime
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# # from reviews_ratings.models import Review

# Tenant = settings.AUTH_USER_MODEL
# # Create your models here.
# class TenantManager(BaseUserManager):
#     def create_user(self, email,is_admin=False,is_superuser=False, password=None):
#         if not email:
#             raise ValueError('An email address is required')

#         if not password:
#             raise ValueError('Kindly put a password')

#         user_obj = self.model(
#             self.normalize_email(email)

#         )
#         user_obj.set_password(password)
#         user_obj.admin = is_admin,
#         use_objr.superuser = is_superuser,
#         user_obj.save(using=self._db)
#         return user_obj

#     def create_superuser(self, email, password=None):
#         user = self.create_user (
#             email,
#             password = password)
#         user.save(using=self._db)
#         return user


# class Tenant(AbstractBaseUser):
#     review = models.ForeignKey('reviews_ratings.Review', related_name = 'Tenant', null=True, on_delete = models.DO_NOTHING)
#     email = models.EmailField(max_length=200, unique=True)
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     date_joined = models.DateTimeField(default=datetime.now, blank = True)
#     photo = models.ImageField(upload_to='photos/%Y/%m/&d/')
#     admin = models.BooleanField(default = False)
#     superuser =  models.BooleanField(default = False)
    

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = TenantManager()

#     def __str__(self):
#         return self.email

#     def get_full_name(self):
#         return self.first_name

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     @property
#     def is_admin(self):
#         return self.admin

#     @property
#     def is_superuser(self):
#         return self.superuser

    
