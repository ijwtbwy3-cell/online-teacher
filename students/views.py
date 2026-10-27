from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from attendance.models import AttendanceRecord
from assignments.models import Assignment
from exams.models import Exam
from quizzes.models import Quiz
from .models import Student


@login_required
def student_list(request):
    return render(request, 'students/list.html', {'students': Student.objects.all()})


@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk = pk)
    batches = student.batches.all()
    attendance_records = list(AttendanceRecord.objects.filter(student = student).order_by('-session__date'))
    quizzes = Quiz.objects.filter(batch__students = student)
    exams = Exam.objects.filter(batch__students = student)
    assignments = Assignment.objects.filter(batch__students = student)
    attendance = {'total': 0, 'attended': 0, 'missed': 0}
    for record in attendance_records:
        attendance['total'] += 1
        if record.status == 'present':
            attendance['attended'] += 1
        elif record.status == 'absent':
            attendance['missed'] += 1

    attendance['percentage'] = 0
    if attendance['total'] > 0:
        attendance['percentage'] = (attendance['attended'] * 100 / attendance['total'])

    submissions = student.submissions.all()

    return render(request, 'students/detail.html', {
        'student': student,
        'batches': batches,
        'attendance': attendance,
        'attendance_records': attendance_records,
        'submissions': submissions,
        'quizzes': quizzes,
        'exams': exams,
        'assignments': assignments,
    })
