from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from batches.models import Batch
from .models import Exam


@login_required
def exam_list(request):
    search_query = request.GET.get('q', '').strip()
    exams = Exam.objects.filter(title__icontains = search_query)
    return render(request, 'exams/list.html', {'exams': exams,'search_query': search_query,})


@login_required
def exam_detail(request, pk):
    exam = get_object_or_404(Exam, pk = pk)
    return render(request, 'exams/detail.html', {'exam': exam})


@login_required
def exam_created(request, pk):
    exam = get_object_or_404(Exam, pk = pk)
    return render(request, 'exams/created.html', {'exam': exam})


@login_required
def exam_create(request):
    batches = Batch.objects.all()
    if request.method == 'POST':
        batch = Batch.objects.filter(pk = request.POST.get('batch')).first()
        start_at = request.POST.get('start_at')
        end_at = request.POST.get('end_at')
        if not start_at:
            start_at = None
        if not end_at:
            end_at = None

        exam = Exam.objects.create(
            title = request.POST['title'],
            course = request.POST.get('course', ''),
            subject = request.POST.get('subject', ''),
            batch = batch,
            created_by = request.user,
            start_at = start_at,
            end_at = end_at,
            total_marks = request.POST.get('total_marks', 100),
            is_published = request.POST.get('is_published') == 'on',
        )
        return redirect('exam_created', pk = exam.pk)
    return render(request, 'exams/form.html', {'batches': batches})
