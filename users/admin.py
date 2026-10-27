from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as Base
from .models import User
@admin.register(User)
class UserAdmin(Base):
    list_display = ['username', 'email', 'role', 'is_staff']