from rest_framework.viewsets import ModelViewSet

from exams.models import Exam
from exams.serializers import ExamSerializer


class ExamViewSet(ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
