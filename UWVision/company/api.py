from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Company
from .serializers import CompanySerializer
from django.core import serializers

@api_view(['GET'])
def get_all_companies(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

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
