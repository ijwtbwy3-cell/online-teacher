from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField(unique = True)
    phone = models.CharField(max_length = 20, blank = True)
    status = models.CharField(max_length = 20, default = 'active')
    notes = models.TextField(blank = True)
    enrollment_date = models.DateField(auto_now_add = True)
    created_at = models.DateTimeField(auto_now_add = True)
    class Meta:
        ordering = ['-created_at']

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()
