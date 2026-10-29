from rest_framework import serializers
from doubts.models import Doubt


class DoubtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doubt
        fields = '__all__'
        read_only_fields = ('answered_by', 'created_at', 'answered_at')
