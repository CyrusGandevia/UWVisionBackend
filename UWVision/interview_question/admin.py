from django.contrib import admin
from .models import InterviewQuestion, UpvotedInterviewQuestion

# Register your models here.
class InterviewQuestionAdmin(admin.ModelAdmin):
    search_fields = ['job_id', 'body', 'program']
    list_display = [
        'id',
        'job_id',
        'body',
        'year_worked',
        'term_worked',
        'coop_term_number',
        'program',
        'created_at',
        'added_by'
    ]
    list_filter = ['year_worked', 'term_worked', 'coop_term_number', 'program']

class UpvotedInterviewQuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'interview_question_id', 'user_id']

admin.site.register(InterviewQuestion, InterviewQuestionAdmin)
admin.site.register(UpvotedInterviewQuestion, UpvotedInterviewQuestionAdmin)
