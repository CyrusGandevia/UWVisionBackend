from django.urls import path
from .api import get_all_jobs_for_company, get_all_saved_jobs, create_job, get_job, save_job

urlpatterns = [
    # GET requests:
    path('get/company/<slug:company_name>/job/all', get_all_jobs_for_company),
    path('get/company/<slug:company_name>/job/<slug:job_name>', get_job),
    path('get/job/saved/all', get_all_saved_jobs),

    # POST requests:
    path('post/job', create_job),
    path('post/job/save', save_job)
]