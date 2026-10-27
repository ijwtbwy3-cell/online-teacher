from django.contrib import admin
from .models import Task, TaskPriority, TaskStatus

admin.site.register((Task, TaskStatus, TaskPriority))
