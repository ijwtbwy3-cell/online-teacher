from rest_framework.viewsets import ModelViewSet
from doubts.models import Doubt
from doubts.serializers import DoubtSerializer


class DoubtViewSet(ModelViewSet):
    queryset = Doubt.objects.all()
    serializer_class = DoubtSerializer
