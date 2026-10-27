from django.db import models
from django.conf import settings
from batches.models import Batch

class Quiz(models.Model):
    title = models.CharField(max_length = 255)
    course = models.CharField(max_length = 255, blank = True)
    subject = models.CharField(max_length = 255, blank = True)
    batch = models.ForeignKey(Batch, on_delete = models.SET_NULL, null = True, blank = True, related_name = 'quizzes')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.SET_NULL, null = True)
    start_at = models.DateTimeField(null = True, blank = True)
    end_at = models.DateTimeField(null = True, blank = True)
    questions_count = models.PositiveIntegerField(default = 0)
    passing_percentage = models.PositiveIntegerField(default = 70)
    is_published = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Quizzes'
    def __str__(self):
        return self.title
