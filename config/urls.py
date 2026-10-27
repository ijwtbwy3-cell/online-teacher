from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from config.api_urls import api_router
from core.views import dashboard
from users.views import login_view, logout_view, profile_view
from liveclasses.views import liveclass_list, liveclass_detail, liveclass_create
from quizzes.views import quiz_list, quiz_detail, quiz_create, quiz_created
from exams.views import exam_list, exam_detail, exam_create, exam_created
from assignments.views import assignment_list, assignment_detail, assignment_create, assignment_created
from batches.views import batch_list, batch_detail
from students.views import student_list, student_detail
from doubts.views import doubt_list, doubt_detail
from tasks.views import task_list, task_update_status
from schedule.views import schedule_view
from attendance.views import attendance_list

schema_view = get_schema_view(
    openapi.Info(
        title = 'Online Teacher',
        default_version = 'v1',
    ),
    public = True,
    permission_classes = (permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout = 0), name = 'swagger-ui'),
    path('api/', include(api_router.urls)),
    path('', dashboard, name = 'dashboard'),
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('profile/', profile_view, name = 'profile'),
    path('live-classes/', liveclass_list, name = 'liveclass_list'),
    path('live-classes/add/', liveclass_create, name = 'liveclass_create'),
    path('live-classes/<int:pk>/', liveclass_detail, name = 'liveclass_detail'),
    path('schedule/', schedule_view, name = 'schedule'),
    path('quizzes/', quiz_list, name = 'quiz_list'),
    path('quizzes/add/', quiz_create, name = 'quiz_create'),
    path('quizzes/<int:pk>/created/', quiz_created, name = 'quiz_created'),
    path('quizzes/<int:pk>/', quiz_detail, name = 'quiz_detail'),
    path('exams/', exam_list, name = 'exam_list'),
    path('exams/add/', exam_create, name = 'exam_create'),
    path('exams/<int:pk>/created/', exam_created, name = 'exam_created'),
    path('exams/<int:pk>/', exam_detail, name = 'exam_detail'),
    path('assignments/', assignment_list, name = 'assignment_list'),
    path('assignments/add/', assignment_create, name = 'assignment_create'),
    path('assignments/<int:pk>/created/', assignment_created, name = 'assignment_created'),
    path('assignments/<int:pk>/', assignment_detail, name = 'assignment_detail'),
    path('batches/', batch_list, name = 'batch_list'),
    path('batches/<int:pk>/', batch_detail, name = 'batch_detail'),
    path('students/', student_list, name = 'student_list'),
    path('students/<int:pk>/', student_detail, name = 'student_detail'),
    path('doubts/', doubt_list, name = 'doubt_list'),
    path('doubts/<int:pk>/', doubt_detail, name = 'doubt_detail'),
    path('tasks/', task_list, name = 'task_list'),
    path('tasks/<int:pk>/status/', task_update_status, name = 'task_update_status'),
    path('attendance/', attendance_list, name = 'attendance_list'),
]