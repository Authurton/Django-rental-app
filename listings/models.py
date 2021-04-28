from django.db import models
from datetime import datetime
from django.conf import settings
# from reviews_ratings.models import Review
from accounts.models import Landlord, Tenant 
# from reviews_ratings.models import Comment

# Create your models here.
class Listing(models.Model):
    landlord = models.ForeignKey(Landlord, on_delete = models.CASCADE, null=True, blank=True)
    # comment = models.ForeignKey(Comment, related_name="Listing",on_delete = models.DO_NOTHING)
    tenant = models.ForeignKey(Tenant, on_delete=models.DO_NOTHING, null=True, blank=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    price = models.IntegerField()
    wifi = models.CharField(max_length=200)
    room_type = models.CharField(max_length=200)
    bedroom = models.IntegerField(default = 1)
    bathroom = models.IntegerField(default=1)
    garage = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now,blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/&d')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/&d')
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/&d')
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/&d')
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/&d', blank = True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/&d', blank = True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/&d', blank = True)

    # listing = models.Manager()
    objects =  models.Manager()
    def __str__(self):
        return self.address

    # def is_activated(self):
    #     if self.wifi == 'wifi':
    #         return True
    #     return False

    #     is_acivated.boolean = True


    

        




