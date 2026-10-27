from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import AttendanceSession


@login_required
def attendance_list(request):
    sessions = AttendanceSession.objects.all()
    return render(request, 'attendance/list.html', {'sessions': sessions})
