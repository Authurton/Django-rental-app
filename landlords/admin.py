# from django.contrib import admin
# # from django.contrib.auth.models import Group
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .models import Landlord

# # User = get_user_model

# # Register your models here.
# class LandlordAdmin(BaseUserAdmin):
#     model = Landlord
#     list_display = ('email', 'admin')
#     list_filter = ('staff','admin', 'active')

#     fieldsets = (
#         (None, {"fields": ('email', 'password'),}),
#         ('Permissions',{'fields': ('admin', 'staff', 'active', 'superuser')}),
        
#     )

#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2')
#         },

#         ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
#     filter_horizontal = ()

# admin.site.register(Landlord, LandlordAdmin)
# # admin.site.unregister(Group)