from rest_framework.viewsets import ModelViewSet
from assignments.models import Assignment, Submission
from attendance.models import AttendanceRecord, AttendanceSession
from batches.models import Batch
from doubts.models import Doubt
from exams.models import Exam
from liveclasses.models import LiveClass
from quizzes.models import Quiz
from students.models import Student
from tasks.models import Task, TaskPriority, TaskStatus
from config.serializers import (AssignmentSerializer,AttendanceRecordSerializer,AttendanceSessionSerializer,BatchSerializer,DoubtSerializer,ExamSerializer,LiveClassSerializer,QuizSerializer,StudentSerializer,SubmissionSerializer,TaskPrioritySerializer,TaskSerializer,TaskStatusSerializer,)


class LiveClassViewSet(ModelViewSet):
    queryset = LiveClass.objects.all()
    serializer_class = LiveClassSerializer

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)


class QuizViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ExamViewSet(ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class AssignmentViewSet(ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class SubmissionViewSet(ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer


class BatchViewSet(ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class AttendanceSessionViewSet(ModelViewSet):
    queryset = AttendanceSession.objects.all()
    serializer_class = AttendanceSessionSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class AttendanceRecordViewSet(ModelViewSet):
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer


class DoubtViewSet(ModelViewSet):
    queryset = Doubt.objects.all()
    serializer_class = DoubtSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TaskStatusViewSet(ModelViewSet):
    queryset = TaskStatus.objects.all()
    serializer_class = TaskStatusSerializer


class TaskPriorityViewSet(ModelViewSet):
    queryset = TaskPriority.objects.all()
    serializer_class = TaskPrioritySerializer
