from rest_framework.routers import DefaultRouter    
from config.api import (AssignmentViewSet,AttendanceRecordViewSet,AttendanceSessionViewSet,BatchViewSet,DoubtViewSet,ExamViewSet,LiveClassViewSet,QuizViewSet,StudentViewSet,SubmissionViewSet,TaskPriorityViewSet,TaskStatusViewSet,TaskViewSet,)


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
