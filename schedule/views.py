from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from liveclasses.models import LiveClass


@login_required
def schedule_view(request):
    columns = []
    statuses = [
        ('not_started', 'Not Started', 'bg-slate-500'),
        ('starting_soon', 'Starting Soon', 'bg-amber-500'),
        ('ongoing', 'Ongoing', 'bg-blue-500'),
        ('completed', 'Completed', 'bg-emerald-500'),
        ('cancelled', 'Cancelled', 'bg-rose-600'),
    ]

    for code, label, header in statuses:
        columns.append({
            'label': label,
            'header_class': header,
            'live_classes': LiveClass.objects.filter(status = code).order_by('scheduled_at'),
        })

    return render(request, 'schedule/list.html', {'columns': columns})
