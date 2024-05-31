from rest_framework import serializers
from .models import SafetyProfile

class SafetyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SafetyProfile
        fields = '__all__'
