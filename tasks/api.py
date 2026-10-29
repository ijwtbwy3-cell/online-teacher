from rest_framework.viewsets import ModelViewSet

from tasks.models import Task, TaskPriority, TaskStatus
from tasks.serializers import TaskPrioritySerializer, TaskSerializer, TaskStatusSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskStatusViewSet(ModelViewSet):
    queryset = TaskStatus.objects.all()
    serializer_class = TaskStatusSerializer


class TaskPriorityViewSet(ModelViewSet):
    queryset = TaskPriority.objects.all()
    serializer_class = TaskPrioritySerializer
