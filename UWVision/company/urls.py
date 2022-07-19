from django.urls import path
from .api import get_searchbar_data, get_company_data, create_company

urlpatterns = [
    # GET requests:
    path('get/searchbar_data', get_searchbar_data),
    path('get/company/<int:company_id>', get_company_data),

    # POST requests:
    path('create/company', create_company)
]