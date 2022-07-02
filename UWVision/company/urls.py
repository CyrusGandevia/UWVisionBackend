from django.urls import path
from .api import get_all_companies, create_company

urlpatterns = [
    path('get', get_all_companies),
    path('create', create_company)
]