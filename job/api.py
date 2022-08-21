from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from django.db.models import Count, Avg, F, Sum, Func
from django.core.exceptions import ObjectDoesNotExist

from .models import Company, Job, SavedJob
from .serializers import JobSerializer, SavedJobSerializer

from collections import defaultdict

# Functionality for rounding to two decimal places for the Avg() functions
class Round(Func):
    function = "ROUND"
    template = "%(function)s(%(expressions)s::numeric, 2)"

@api_view(['GET'])
@permission_classes([])
def get_all_jobs_for_company(request, **kwargs):
    # If company name is not passed
    company_name = kwargs.get('company_name', None)
    if not company_name:
        return Response({'error': 'No company name passed!'}, status=status.HTTP_400_BAD_REQUEST)

    # Replace truncated name (that would have spaces, ex: Jane-Street => Jane Street)
    company_name = company_name.replace("-", " ");

    # Get all jobs for current company, each populated with the following metrics:
    # - Average hourly wage for the job
    # - Number of salaries posted for the job
    # - Average rating for the job
    # - Number of reviews posted for the job
    jobs = (Job
            .objects
            .filter(company__name=company_name)
            .values('id', 'name')
            .annotate(avg_hourly_wage=Round(Avg('salary__hourly_wage')), 
                    salary_count=Count('salary__id', distinct=True))
            .annotate(avg_overall_rating=Round(Avg('review__overall_rating')), 
                    review_count=Count('review__id', distinct=True)))

    # If user is passed in authentication header, we want to also identify if the fetched jobs are saved jobs
    if request.user.id:
        saved_jobs = SavedJob.objects.filter(user_id=request.user.id)
        
        for job in jobs:
            job['saved'] = saved_jobs.filter(job_id=job["id"]).exists()


    # We also want some aggregated metrics for the company:
    # - Overall rating based on all reviews
    # - Number of reviews
    company_summary = jobs.aggregate(avg_company_rating=Round(Avg('avg_overall_rating')), overall_review_count=Sum('review_count', distinct=True))
    
    return Response({'company_summary': company_summary, 'jobs': list(jobs)}, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_job(request):
    # Create object from request payload
    data = {
        'company': request.data.get('company'), # primary key
        'name': request.data.get('name'),
        'added_by': request.user.id
    }

    # Validate data against serializer
    serializer = JobSerializer(data=data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Create object
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([])
def get_job(request, **kwargs):
    # If company name or job name is not passed
    company_name = kwargs.get('company_name', None)
    job_name = kwargs.get('job_name', None)

    if not company_name or not job_name:
        return Response({'error': 'No company name or job name passed!'}, status=status.HTTP_400_BAD_REQUEST)

    # Replace truncated names (that would have spaces, 
    #   ex. Jane-Street => Jane Street
    #   ex. Software-Engineering-Intern => Software Engineering Intern
    # )
    company_name = company_name.replace("-", " ")
    job_name = job_name.replace("-", " ")

    # Get job, if exists
    try:
        company = Company.objects.values().get(name=company_name)
        try:
            job = Job.objects.values().get(company_id=company['id'], name=job_name)
            return Response(data=job, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'error': 'Job with name=' + job_name + ' does not exist.'}, status=status.HTTP_404_NOT_FOUND)
    except ObjectDoesNotExist:
        return Response({'error': 'Company with name=' + company_name + ' does not exist.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_all_saved_jobs(request):
    user_id = request.user.id

    # Get all saved jobs that the user has saved, each populated with the following metrics:
    # - Average hourly wage for the job
    # - Number of salaries posted for the job
    # - Average rating for the job
    # - Number of reviews posted for the job
    saved_jobs = (SavedJob
                  .objects
                  .filter(user_id=user_id)
                  .values('job_id', company=F('job__company__name'), name=F('job__name'))
                  .annotate(avg_hourly_wage=Round(Avg('job__salary__hourly_wage')), 
                            salary_count=Count('job__salary__id', distinct=True))
                  .annotate(avg_overall_rating=Round(Avg('job__review__overall_rating')), 
                            review_count=Count('job__review__id', distinct=True)))
    
    # Group the jobs by their respective company
    saved_jobs_grouped_by_company = defaultdict(list)
    for job in saved_jobs:
        saved_jobs_grouped_by_company[job['company']].append(job)

    return Response(saved_jobs_grouped_by_company, status=status.HTTP_200_OK)

@api_view(['POST'])
def save_job(request): # Also unsaves the review if already exists
    # Create object from request payload
    data = {
        'job': request.data.get('job'), # primary key
        'user': request.user.id
    }

    # Validate data against serializer
    serializer = SavedJobSerializer(data=data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Save/Unsave Logic:
    saved_job = SavedJob.objects.filter(job=data['job'], user=data['user'])
    # If job already exists, we unsave it
    if saved_job:
        saved_job.delete()
        return Response({'response': 'unsaved job'}, status=status.HTTP_200_OK)
    else: # Otherwise, we save it
        serializer.save()
        return Response({'response': 'saved job'}, status=status.HTTP_201_CREATED)
