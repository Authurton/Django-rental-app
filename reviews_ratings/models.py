from django.db import models
from django.utils import timezone
from datetime import datetime
from django.urls import reverse
from accounts.models import Tenant, User
from listings.models import Listing
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

# class Post(models.Model):
    
# 	tenant = models.ForeignKey('auth.User', on_delete=models.CASCADE)
# 	text = models.TextField()
# 	create_date = models.DateTimeField(default=timezone.now())
# 	published_date = models.DateTimeField(blank=True,null=True)
    

# 	def publish(self):
# 		self.published_date = timezone.now()
# 		self.save()


# 	def approve_comments(self):
# 		return self.comments.filter(approved_comment=True)

# 	def get_absolute_url(self):
# 		return reverse('post_detail',kwargs={'pk':self.pk})

# 	def __str__(self):
# 		return self.tenant

class Comment(models.Model):
    rating = models.FloatField(default=0)
    listing = models.ForeignKey(Listing, related_name="comments", on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    text = models.TextField(max_length=300, null=True, blank=True)
    create_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        self.tenant