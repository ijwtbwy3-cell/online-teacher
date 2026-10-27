from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Batch


@login_required
def batch_list(request):
    search_query = request.GET.get('q', '').strip()
    batches = Batch.objects.filter(name__icontains = search_query)
    return render(request, 'batches/list.html', {
        'batches': batches,
        'search_query': search_query,
    })


@login_required
def batch_detail(request, pk):
    batch = get_object_or_404(Batch, pk = pk)
    return render(request, 'batches/detail.html',
    {'batch': batch})
