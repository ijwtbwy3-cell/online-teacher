from rest_framework.viewsets import ModelViewSet

from batches.models import Batch
from batches.serializers import BatchSerializer


class BatchViewSet(ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
