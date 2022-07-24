from django.urls import path
from .api import get_companies, get_company, create_company

urlpatterns = [
    # GET requests:
    path('get/company/all', get_companies),
    path('get/company/<slug:company_name>', get_company),

    # POST requests:
    path('post/company', create_company)
]