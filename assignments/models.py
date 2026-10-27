from django.db import models
from django.conf import settings
from batches.models import Batch
from students.models import Student


class Assignment(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField(blank = True)
    course = models.CharField(max_length = 255, blank = True)
    subject = models.CharField(max_length = 255, blank = True)
    batch = models.ForeignKey(Batch, on_delete = models.SET_NULL, null = True, blank = True, related_name = 'assignments')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.SET_NULL, null = True)
    due_date = models.DateTimeField(null = True, blank = True)
    max_marks = models.PositiveIntegerField(default = 100)
    status = models.CharField(max_length = 20, default = 'draft')
    created_at = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.title

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete = models.CASCADE, related_name = 'submissions')
    student = models.ForeignKey(Student, on_delete = models.CASCADE, related_name = 'submissions')
    content = models.TextField(blank = True)
    marks_obtained = models.DecimalField(max_digits = 6, decimal_places = 2, null = True, blank = True)
    submitted_at = models.DateTimeField(auto_now_add = True)