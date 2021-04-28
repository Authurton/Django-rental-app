
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Landlord
from .models import Tenant
from .models import User

# User = get_user_model

# Register your models here.
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('first_name', 'last_name', 'email','admin',)
    list_filter = ('staff','admin', 'active')

    fieldsets = (
        (None, {"fields": ('email', 'password'),}),
        ('Permissions',{'fields': ('admin', 'staff', 'active', 'superuser')}),
        
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        },

        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)

class LandlordAdmin(admin.ModelAdmin):
    model = Landlord
    list_display = ('first_name','last_name','email','phone', 'whatsapp')
    list_display_links = ('first_name',)
    search_fields = ('full_name',)
    list_per_page = 25

admin.site.register(Landlord, LandlordAdmin)


class TenantAdmin(admin.ModelAdmin):
    model = Tenant
    list_display = ('first_name', 'last_name','email', 'date_joined')
    list_display_links = ('first_name',)
    search_fields = ('full_name',)
    list_per_page = 25

admin.site.register(Tenant, TenantAdmin)

