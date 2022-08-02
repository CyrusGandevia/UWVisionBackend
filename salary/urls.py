from django.urls import path
from .api import get_all_salaries_for_job, create_salary

urlpatterns = [
    # GET requests:
    path('get/job/<int:job_id>/salary/all', get_all_salaries_for_job),

    # POST requests:
    path('post/salary', create_salary)
]