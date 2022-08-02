from django.urls import path
from .api import get_all_interview_questions_for_job, create_interview_question, upvote_interview_question

urlpatterns = [
    # GET requests:
    path('get/job/<int:job_id>/interview_question/all', get_all_interview_questions_for_job),

    # POST requests:
    path('post/interview_question', create_interview_question),
    path('post/interview_question/upvote', upvote_interview_question)
]