from rest_framework.routers import DefaultRouter
from assignments.api import AssignmentViewSet, SubmissionViewSet
from attendance.api import AttendanceRecordViewSet, AttendanceSessionViewSet
from batches.api import BatchViewSet
from doubts.api import DoubtViewSet
from exams.api import ExamViewSet
from liveclasses.api import LiveClassViewSet
from quizzes.api import QuizViewSet
from students.api import StudentViewSet
from tasks.api import TaskPriorityViewSet, TaskStatusViewSet, TaskViewSet

api_router = DefaultRouter()
api_router.register('live-classes', LiveClassViewSet)
api_router.register('quizzes', QuizViewSet)
api_router.register('exams', ExamViewSet)
api_router.register('assignments', AssignmentViewSet)
api_router.register('submissions', SubmissionViewSet)
api_router.register('batches', BatchViewSet)
api_router.register('students', StudentViewSet)
api_router.register('attendance-sessions', AttendanceSessionViewSet)
api_router.register('attendance-records', AttendanceRecordViewSet)
api_router.register('doubts', DoubtViewSet)
api_router.register('tasks', TaskViewSet)
api_router.register('task-statuses', TaskStatusViewSet)
api_router.register('task-priorities', TaskPriorityViewSet)
