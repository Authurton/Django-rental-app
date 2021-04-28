from django.contrib import admin
from .models import Listing
from accounts.models import Landlord
from reviews_ratings.models import Comment
# from reviews_ratings.models import Review

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'price', 'address', 'landlord', 'wifi',)
    list_display_links = ('id', 'address') 
    search_fields = ('address','city')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)
