from django.urls import path
from . import views

# app_name = 'accounts'

urlpatterns = [
    path('register', views.register, name='register'),
    #  path('create',views.create, name='create'),
    path('login', views.login, name='login'),
    path('dashboard',views.dashboard, name='dashboard'),
    path("landlord_dash", views.landlord_dash, name="landlord_dash"),
    path('logout', views.logout, name='logout'),
    path("login_after", views.login_after, name="login_after"),
    path("landlord_edit/<int:user_id>", views.landlord_edit, name="landlord_edit"),
    path('listing_dashboard/<int:user_id>', views.listing_dashboard, name='listing_dashboard'),
    path('landlord_update/<int:user_id>', views.landlord_update, name='landlord_update'),
    path("land_diff/<int:user_id>", views.land_diff, name="land_diff"),
    path("edit_info/<int:user_id>", views.edit_info, name="edit_info"),
    path("edit_info_save/<int:user_id>", views.edit_info_save, name="edit_info_save")
    # path("listings", views.landlord_dash, name="landlord_dash")
    
]