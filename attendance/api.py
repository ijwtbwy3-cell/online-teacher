from rest_framework.viewsets import ModelViewSet
from attendance.models import AttendanceRecord, AttendanceSession
from attendance.serializers import AttendanceRecordSerializer, AttendanceSessionSerializer


class AttendanceSessionViewSet(ModelViewSet):
    queryset = AttendanceSession.objects.all()
    serializer_class = AttendanceSessionSerializer


class AttendanceRecordViewSet(ModelViewSet):
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer
