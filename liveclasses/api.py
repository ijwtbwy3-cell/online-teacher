from rest_framework.viewsets import ModelViewSet
from liveclasses.models import LiveClass
from liveclasses.serializers import LiveClassSerializer


class LiveClassViewSet(ModelViewSet):
    queryset = LiveClass.objects.all()
    serializer_class = LiveClassSerializer
