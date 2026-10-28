from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from batches.models import Batch
from .models import LiveClass


LIVE_CLASS_STATUSES = (
    ('not_started', 'Not Started'),
    ('starting_soon', 'Starting Soon'),
    ('ongoing', 'Ongoing'),
    ('completed', 'Completed'),
    ('cancelled', 'Cancelled'),
)


@login_required
def liveclass_list(request):
    selected_tab = request.GET.get('tab', 'scheduled')
    search_query = request.GET.get('q', '').strip()
    if selected_tab == 'history':
        live_classes = LiveClass.objects.filter(status = 'completed')
    else:
        live_classes = LiveClass.objects.exclude(status = 'completed')

    return render(request, 'liveclasses/list.html', {
        'live_classes': live_classes.filter(title__icontains = search_query),
        'selected_tab': selected_tab,
        'search_query': search_query,
    })


@login_required
def liveclass_detail(request, pk):
    live_class = get_object_or_404(LiveClass, pk = pk)
    if request.method == 'POST':
        status = request.POST.get('status')
        if status in dict(LIVE_CLASS_STATUSES):
            live_class.status = status
            live_class.save(update_fields = ['status'])
            messages.success(request, 'Class status updated')
            return redirect('liveclass_detail', pk = live_class.pk)
        messages.error(request, 'Please select a valid status')
    return render(request, 'liveclasses/detail.html', {
        'live_class': live_class,
        'statuses': LIVE_CLASS_STATUSES,
    })


@login_required
def liveclass_create(request):
    batches = Batch.objects.all()
    if request.method == 'POST':
        batch_id = request.POST.get('batch')
        batch = batches.filter(pk = batch_id).first()
        if batch_id and not batch:
            messages.error(request, 'Please select a valid batch')
            return render(request, 'liveclasses/form.html', {'batches': batches})

        LiveClass.objects.create(
            title = request.POST['title'],
            batch = batch,
            teacher = request.user,
            scheduled_at = request.POST['scheduled_at'],
            duration_minutes = request.POST.get('duration_minutes', 60),
        )
        messages.success(request, 'Class created')
        return redirect('liveclass_list')
    return render(request, 'liveclasses/form.html', {'batches': batches})
