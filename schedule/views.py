from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from liveclasses.models import LiveClass


@login_required
def schedule_view(request):
    statuses = [
        {'status': 'not_started', 'label': 'Not Started', 'header_class': 'bg-slate-500'},
        {'status': 'starting_soon', 'label': 'Starting Soon', 'header_class': 'bg-amber-500'},
        {'status': 'ongoing', 'label': 'Ongoing', 'header_class': 'bg-blue-500'},
        {'status': 'completed', 'label': 'Completed', 'header_class': 'bg-emerald-500'},
        {'status': 'cancelled', 'label': 'Cancelled', 'header_class': 'bg-rose-600'},
    ]

    columns = []
    for status in statuses:
        column = {
            'label': status['label'],
            'header_class': status['header_class'],
            'live_classes': LiveClass.objects.filter(status = status['status']).order_by('scheduled_at'),
        }
        columns.append(column)

    return render(request, 'schedule/list.html', {'columns': columns})
