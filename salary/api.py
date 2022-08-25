from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from .models import Salary
from .serializers import SalarySerializer

@api_view(['GET'])
@permission_classes([])
def get_all_salaries_for_job(request, **kwargs):
    # If job id is not passed
    job_id = kwargs.get('job_id', None)
    if not job_id:
        return Response({'error': 'No job id passed!'}, status=status.HTTP_400_BAD_REQUEST)

    salaries = Salary.objects.filter(job__id=job_id).values()
    return Response(data=salaries, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_salary(request):
    # Create object from request payload
    data = {
        'job': request.data.get('job'), # primary key
        'hourly_wage': request.data.get('hourly_wage'),
        'monthly_relocation_stipend': request.data.get('monthly_relocation_stipend'),
        'monthly_misc_stipends': request.data.get('monthly_misc_stipends'),
        'term_signing_bonus': request.data.get('term_signing_bonus'),
        'city': request.data.get('city'),
        'country': request.data.get('country'),
        'year_worked': request.data.get('year_worked'),
        'term_worked': request.data.get('term_worked'),
        'coop_term_number': request.data.get('coop_term_number'),
        'program': request.data.get('program'),
        'added_by': request.user.id,
    }

    # Validate data against serializer
    serializer = SalarySerializer(data=data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Create object
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    