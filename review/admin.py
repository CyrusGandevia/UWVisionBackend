from django.contrib import admin
from .models import Review, UpvotedReview

class ReviewAdmin(admin.ModelAdmin):
    search_fields = ['job', 'body', 'program']
    list_display = [
        'id',
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
    list_filter = ['year_worked', 'term_worked', 'coop_term_number', 'program']

class UpvotedReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'review', 'user']

admin.site.register(Review, ReviewAdmin)
admin.site.register(UpvotedReview, UpvotedReviewAdmin)