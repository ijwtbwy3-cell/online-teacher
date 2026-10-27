from django.db import models
from django.conf import settings
from students.models import Student
from batches.models import Batch


class Doubt(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE, related_name = 'doubts')
    batch = models.ForeignKey(Batch, on_delete = models.SET_NULL, null = True, blank = True)
    title = models.CharField(max_length = 255)
    description = models.TextField()
    status = models.CharField(max_length = 20, default = 'open')
    answer = models.TextField(blank = True)
    answered_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.SET_NULL, null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
    answered_at = models.DateTimeField(null = True, blank = True)
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.title
