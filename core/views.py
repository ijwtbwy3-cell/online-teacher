from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from liveclasses.models import LiveClass
from tasks.models import Task, TaskStatus
from batches.models import Batch


@login_required
def dashboard(request):
    selected_task_status = request.GET.get('task_status', 'all')

    if selected_task_status == 'all':
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(status__code = selected_task_status)

    task_statuses = TaskStatus.objects.all()
    live_classes = LiveClass.objects.exclude(status = 'completed').order_by('scheduled_at')
    batches = Batch.objects.filter(status = 'active')

    return render(request, 'core/dashboard.html', {
        'live_classes': live_classes,
        'tasks': tasks,
        'task_statuses': task_statuses,
        'batches': batches,
        'selected_task_status': selected_task_status,
    })
