from rest_framework.viewsets import ModelViewSet

from assignments.models import Assignment, Submission
from assignments.serializers import AssignmentSerializer, SubmissionSerializer


class AssignmentViewSet(ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer


class SubmissionViewSet(ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
