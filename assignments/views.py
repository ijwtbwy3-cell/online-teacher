from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from batches.models import Batch
from .models import Assignment


@login_required
def assignment_list(request):
    search_query = request.GET.get('q', '').strip()
    assignments = Assignment.objects.filter(title__icontains = search_query)
    return render(request, 'assignments/list.html', {
        'assignments': assignments,
        'search_query': search_query,
    })


@login_required
def assignment_detail(request, pk):
    assignment = get_object_or_404(Assignment, pk = pk)
    return render(request, 'assignments/detail.html', {
        'assignment': assignment,
        'submissions': assignment.submissions.all(),
    })


@login_required
def assignment_create(request):
    batches = Batch.objects.all()
    if request.method == 'POST':
        batch_id = request.POST.get('batch')
        batch = batches.filter(pk = batch_id).first()
        if batch_id and not batch:
            messages.error(request, 'Please select a valid batch')
            return render(request, 'assignments/form.html', {'batches': batches})

        due_date = request.POST.get('due_date')
        if not due_date:
            due_date = None

        assignment = Assignment.objects.create(
            title = request.POST['title'],
            description = request.POST.get('description', ''),
            course = request.POST.get('course', ''),
            subject = request.POST.get('subject', ''),
            batch = batch,
            created_by = request.user,
            max_marks = request.POST.get('max_marks', 100),
            status = 'published' if request.POST.get('is_published') == 'on' else 'draft',
            due_date = due_date,
        )
        return redirect('assignment_created', pk=assignment.pk)
    return render(request, 'assignments/form.html', {'batches': batches})


@login_required
def assignment_created(request, pk):
    assignment = get_object_or_404(Assignment, pk = pk)
    return render(request, 'assignments/created.html', {'assignment': assignment})
