from django.contrib import admin
from .models import Review, UpvotedReview

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    search_fields = ['job_id', 'body', 'program']
    list_display = [
        'id',
        'job_id',
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
    list_display = ['id', 'review_id', 'user_id']

admin.site.register(Review, ReviewAdmin)
admin.site.register(UpvotedReview, UpvotedReviewAdmin)