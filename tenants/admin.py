# from django.contrib import admin
# # from django.contrib.auth.models import Group
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .models import Tenant

# # User = get_user_model


# # Register your models here.
# class TenantAdmin(BaseUserAdmin):
#     model = Tenant
#     list_display = ('email', 'admin')
#     list_filter = ('admin',)

#     fieldsets = (
#         (None, {"fields": ('email', 'password'),}),
#         ('Permissions',{'fields': ('admin', 'superuser',)}),
        
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
    

# admin.site.register(Tenant, TenantAdmin)
# # admin.site.unregister(Group)