from rest_framework import serializers
from assignments.models import Assignment, Submission
from attendance.models import AttendanceRecord, AttendanceSession
from batches.models import Batch
from doubts.models import Doubt
from exams.models import Exam
from liveclasses.models import LiveClass
from quizzes.models import Quiz
from students.models import Student
from tasks.models import Task, TaskPriority, TaskStatus


class LiveClassSerializer(serializers.ModelSerializer):
    teacher = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = LiveClass
        fields = '__all__'
        read_only_fields = ('created_at',)


class QuizSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Quiz
        fields = '__all__'
        read_only_fields = ('created_at',)


class ExamSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Exam
        fields = '__all__'
        read_only_fields = ('created_at',)


class AssignmentSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Assignment
        fields = '__all__'
        read_only_fields = ('created_at',)


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'
        read_only_fields = ('submitted_at',)


class BatchSerializer(serializers.ModelSerializer):
    teacher = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Batch
        fields = '__all__'
        read_only_fields = ('created_at',)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ('enrollment_date', 'created_at')


class AttendanceSessionSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = AttendanceSession
        fields = '__all__'
        read_only_fields = ('created_at',)


class AttendanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceRecord
        fields = '__all__'


class DoubtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doubt
        fields = '__all__'
        read_only_fields = ('answered_by', 'created_at', 'answered_at')


class TaskSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('created_at',)


class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = '__all__'


class TaskPrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskPriority
        fields = '__all__'
