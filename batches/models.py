from django.db import models
from django.conf import settings
from students.models import Student


class Batch(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField(blank = True)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.SET_NULL, null = True, related_name = 'batches')
    students = models.ManyToManyField(Student, related_name = 'batches', blank = True)
    start_date = models.DateField()
    end_date = models.DateField(null = True, blank = True)
    status = models.CharField(max_length = 20, default = 'active')
    subjects_count = models.PositiveIntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add = True)
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.name