from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'mobile_phone', 'is_active', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'mobile_phone')
    list_filter = ('is_active', 'is_staff', 'country')
