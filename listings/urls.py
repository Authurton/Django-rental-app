from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
    path("listing_upload/<int:user_id>", views.listing_upload, name="listing_upload")
]