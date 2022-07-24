from django.urls import path

from .api import get_all_jobs_for_company, get_all_saved_jobs

urlpatterns = [
    # GET requests:
    path('get/company/<slug:company_name>/job/all', get_all_jobs_for_company),
    path('get/job/saved/all', get_all_saved_jobs),
    # path('get/job/<int:job_id>', get_job),
]