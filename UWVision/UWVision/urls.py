"""UWVision URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from company import urls as company_urls
from job import urls as job_urls
from salary import urls as salary_urls
from review import urls as review_urls
from interview_question import urls as interview_question_urls
from user import urls as user_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(company_urls)),
    path('api/', include(job_urls)),
    path('api/', include(salary_urls)),
    path('api/', include(review_urls)),
    path('api/', include(interview_question_urls)),
    path('api/', include(user_urls))
]
