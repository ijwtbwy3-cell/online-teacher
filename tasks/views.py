from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task, TaskStatus


@login_required
def task_list(request):
    selected_status = request.GET.get('status', 'all')
    if selected_status == 'all':
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(status__code = selected_status)

    return render(request, 'tasks/list.html', {
        'tasks': tasks,
        'selected_status': selected_status,
        'statuses': TaskStatus.objects.all(),
        'all_task_count': Task.objects.count(),
    })


@login_required
def task_update_status(request, pk):
    if request.method != 'POST':
        return redirect('task_list')

    task = get_object_or_404(Task, pk = pk)
    status = TaskStatus.objects.filter(code = request.POST.get('status')).first()
    if not status:
        messages.error(request, 'Invalid status')
        return redirect('task_list')

    task.status = status
    task.save()
    messages.success(request, 'Status updated')

    return redirect('task_list')
