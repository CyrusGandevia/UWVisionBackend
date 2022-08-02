from rest_framework import serializers
from .models import Review, UpvotedReview

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'job',
            'body',
            'work_life_balance',
            'culture',
            'interesting_work',
            'overall_rating',
            'year_worked',
            'term_worked',
            'coop_term_number',
            'program',
            'created_at',
            'added_by'
        ]

class UpvotedReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpvotedReview
        fields = ['review', 'user']
