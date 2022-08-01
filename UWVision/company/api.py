from datetime import date
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Company
from .serializers import CompanySerializer
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist

@api_view(['GET'])
@permission_classes([]) # Required to override default requirement of authentication credentials
def get_companies(request):
    # 1) Fetches all companies
    # 2) Joins with all jobs 
    # 3) Groups by company name and aggregates number of jobs per company
    # 4) Returns list of {company_name, company_id, job_count} objects
    companies = Company.objects.values('name', 'id').annotate(job_count=Count('job__name')).order_by('name')
    return Response(data=list(companies), status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([]) # Required to override default requirement of authentication credentials
def get_company(request, **kwargs):
    company_name = kwargs.get('company_name', None)
    if not company_name:
        return Response({'error': 'No company name passed!'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Replace truncated name (that would have spaces, ex: Jane-Street => Jane Street)
    company_name = company_name.replace("-", " ");

    try:
        company = Company.objects.values().get(name=company_name)
        return Response(data=company, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'error': 'Company with name=' + company_name + ' does not exist.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_company(request):
    data = {
        'name': request.data.get('name'),
        'description': request.data.get('description'),
        'industry': request.data.get('industry'),
        'added_by': request.user.id
    }

    serializer = CompanySerializer(data=data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    