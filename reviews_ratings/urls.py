from django.urls import path
from . import views

urlpatterns = [
    path("create_comment/<int:listing_id>/<int:user_id>", views.create_comment, name="create_comment"),
    path("commenting/<int:listing_id>", views.commenting, name="commenting")
    
]