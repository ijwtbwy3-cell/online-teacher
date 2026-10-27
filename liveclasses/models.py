from django.db import models
from django.conf import settings
from batches.models import Batch


class LiveClass(models.Model):
    title = models.CharField(max_length = 255)
    batch = models.ForeignKey(Batch, on_delete = models.CASCADE, related_name = 'live_classes', null = True, blank = True)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.SET_NULL, null = True, related_name = 'live_classes')
    scheduled_at = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField(default = 60)
    status = models.CharField(max_length = 20, default = 'not_started')
    created_at = models.DateTimeField(auto_now_add = True)
    class Meta:
        ordering = ['-scheduled_at']
        verbose_name_plural = 'Live Classes'
    def __str__(self):
        return self.title
