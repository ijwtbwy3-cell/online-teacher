from django.db import models
from django.conf import settings
from batches.models import Batch
from students.models import Student


class AttendanceSession(models.Model):
    batch = models.ForeignKey(Batch, on_delete = models.CASCADE, related_name = 'attendance_sessions')
    date = models.DateField()
    topic = models.CharField(max_length = 255, blank = True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.SET_NULL, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        ordering = ['-date']

class AttendanceRecord(models.Model):
    session = models.ForeignKey(AttendanceSession, on_delete = models.CASCADE, related_name = 'records')
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    status = models.CharField(max_length = 20, default = 'present')