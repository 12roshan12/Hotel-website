from django.contrib import admin
from django.contrib.auth.admin import UserAdmin



# Register your models here.
from .models import *


class UserAccount(UserAdmin):
    list_filter = ['is_employee', 'is_customer']
    list_display = ['first_name', 'last_name', 'email', 'is_employee', 'is_customer']
    ordering = ['first_name']
    search_fields = ['first_name', 'last_name', 'email']
    readonly_fields = ['created_at', 'password']
    list_display_links = ['first_name', 'last_name', 'email']

    add_fieldsets = (
        (None, {
            'classes': (
                'wide'
            ),
            'fields': (
                'first_name', 'last_name', 'email', 'password1', 'password2', 'is_active',
                'is_employee', 'is_customer')
        }),
    )

    fieldsets = (
        (None, {
            'fields': (
                'first_name', 'last_name', 'email', 'password'
            ),
        }),
        ('Permissions', {
            'fields': (
                'is_staff', 'is_active', 'is_employee', 'is_customer'
            )
        }),
    )


class ProfileDetail(admin.ModelAdmin):
    list_display = ['user', 'mobile_number', 'location']




admin.site.register(User, UserAccount)
admin.site.register(Profile, ProfileDetail)
admin.site.register(Enquiry)
admin.site.register(Blog)
admin.site.register(AboutUs)
admin.site.register(Events)
