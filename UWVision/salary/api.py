from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Salary

@api_view(['GET'])
def get_all_salaries_for_job(request, **kwargs):
    job_id = kwargs.get('job_id', None)
    if not job_id:
        return Response({'error': 'No job id passed!'}, status=status.HTTP_400_BAD_REQUEST)

    salaries = Salary.objects.filter(job__id=job_id).values()
    return Response(data=salaries, status=status.HTTP_200_OK)
