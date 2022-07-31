from rest_framework import serializers
from .models import Job, SavedJob

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['company', 'name', 'created_at', 'added_by']

class SavedJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedJob
        fields = ['job', 'user']