from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from batches.models import Batch
from .models import Quiz


@login_required
def quiz_list(request):
    search_query = request.GET.get('q', '').strip()
    quizzes = Quiz.objects.filter(title__icontains = search_query)

    return render(request, 'quizzes/list.html', {
        'quizzes': quizzes,
        'search_query': search_query,
    })


@login_required
def quiz_detail(request, pk):
    quiz = get_object_or_404(Quiz, pk = pk)
    return render(request, 'quizzes/detail.html', {'quiz': quiz})


@login_required
def quiz_created(request, pk):
    quiz = get_object_or_404(Quiz, pk = pk)
    return render(request, 'quizzes/created.html', {'quiz': quiz})


@login_required
def quiz_create(request):
    batches = Batch.objects.all()
    if request.method == 'POST':
        batch_id = request.POST.get('batch')
        batch = batches.filter(pk = batch_id).first()
        if batch_id and not batch:
            messages.error(request, 'Please select a valid batch')
            return render(request, 'quizzes/form.html', {'batches': batches})

        start_at = request.POST.get('start_at')
        end_at = request.POST.get('end_at')
        if not start_at:
            start_at = None
        if not end_at:
            end_at = None

        quiz = Quiz.objects.create(
            title = request.POST['title'],
            course = request.POST.get('course', ''),
            subject = request.POST.get('subject', ''),
            batch = batch,
            created_by = request.user,
            start_at = start_at,
            end_at = end_at,
            questions_count = request.POST.get('questions_count', 0),
            passing_percentage = request.POST.get('passing_percentage', 70),
            is_published = request.POST.get('is_published') == 'on',
        )
        return redirect('quiz_created', pk = quiz.pk)
    return render(request, 'quizzes/form.html', {'batches': batches})
