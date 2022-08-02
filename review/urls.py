from django.urls import path
from .api import get_all_reviews_for_job, create_review, upvote_review

urlpatterns = [
    # GET requests:
    path('get/job/<int:job_id>/review/all', get_all_reviews_for_job),

    # POST requests:
    path('post/review', create_review),
    path('post/review/upvote', upvote_review)
]