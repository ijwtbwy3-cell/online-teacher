from django.db import models
from django.conf import settings


class TaskStatus(models.Model):
    code = models.CharField(max_length = 20, unique = True)
    label = models.CharField(max_length = 50)

    class Meta:
        ordering = ['label']

    def __str__(self):
        return self.label


class TaskPriority(models.Model):
    code = models.CharField(max_length = 20, unique = True)
    label = models.CharField(max_length = 50)

    class Meta:
        ordering = ['label']

    def __str__(self):
        return self.label


class Task(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField(blank = True)
    status = models.ForeignKey(TaskStatus, on_delete = models.PROTECT, related_name = 'tasks')
    priority = models.ForeignKey(TaskPriority, on_delete = models.PROTECT, related_name = 'tasks')
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.SET_NULL, null = True, blank = True, related_name = 'assigned_tasks')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.SET_NULL, null = True, related_name = 'created_tasks')
    assigned_at = models.DateTimeField(null = True, blank = True)
    due_at = models.DateTimeField(null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.title
