from rest_framework.viewsets import ModelViewSet

from quizzes.models import Quiz
from quizzes.serializers import QuizSerializer


class QuizViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
