from rest_framework import serializers
from .models import InterviewQuestion, UpvotedInterviewQuestion

class InterviewQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewQuestion
        fields = [
            'job',
            'body',
            'year_worked',
            'term_worked',
            'coop_term_number',
            'program',
            'created_at',
            'added_by'
        ]

class UpvotedInterviewQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpvotedInterviewQuestion
        fields = ['interview_question', 'user']