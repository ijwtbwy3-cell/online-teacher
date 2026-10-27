from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Doubt


@login_required
def doubt_list(request):
    return render(request, 'doubts/list.html', {'doubts': Doubt.objects.all()})


@login_required
def doubt_detail(request, pk):
    doubt = get_object_or_404(Doubt, pk = pk)
    if request.method == 'POST' and not doubt.answer and request.POST.get('answer'):
        doubt.answer = request.POST.get('answer')
        doubt.status = 'answered'
        doubt.answered_by = request.user
        doubt.answered_at = timezone.now()
        doubt.save()
        messages.success(request, 'Answer saved')
        return redirect('doubt_detail', pk = pk)

    return render(request, 'doubts/detail.html', {'doubt': doubt})
