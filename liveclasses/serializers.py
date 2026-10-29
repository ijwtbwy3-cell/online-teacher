from rest_framework import serializers
from liveclasses.models import LiveClass


class LiveClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveClass
        fields = '__all__'
        read_only_fields = ('teacher', 'created_at')
