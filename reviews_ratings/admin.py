from django.contrib import admin
from .models import Comment
from listings.models import Listing


# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'create_date', 'rating', "text",)
    list_display_links = ('tenant',)
    search_fields = ('tenant',)
    list_per_page = 25

# class RatingAdmin(admin.ModelAdmin):
#     list_display = ('review', 'listing', 'value')
#     list_display_links = ('listing', 'review')
#     search_fields = ('listing',)
#     list_per_page = 25

admin.site.register(Comment, CommentAdmin)
# admin.site.register(Review, ReviewAdmin)