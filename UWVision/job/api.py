from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Job, SavedJob
from django.db.models import Count, Avg, F
from collections import defaultdict

@api_view(['GET'])
def get_all_jobs_for_company(request, **kwargs):
    company_name = kwargs.get('company_name', None)
    if not company_name:
        return Response({'error': 'No company name passed!'}, status=status.HTTP_400_BAD_REQUEST)

    # Get all jobs for current company, each populated with the following metrics:
    # - Average hourly wage for the job
    # - Number of salaries posted for the job
    # - Average rating for the job
    # - Number of reviews posted for the job
    jobs = (Job
            .objects
            .filter(company__name=company_name)
            .values('id', 'name')
            .annotate(avg_hourly_wage=Avg('salary__hourly_wage'), 
                    salary_count=Count('salary__id', distinct=True))
            .annotate(avg_overall_rating=Avg('review__overall_rating'), 
                    review_count=Count('review__id', distinct=True)))

    # We also want some aggregated metrics for the company:
    # - Overall rating based on all reviews
    # - Number of reviews
    company_summary = jobs.aggregate(avg_company_rating=Avg('avg_overall_rating'), overall_review_count=Count('review_count', distinct=True))
    
    return Response({'company_summary': company_summary, 'jobs': list(jobs)}, status=status.HTTP_200_OK)


# TODO: Add job

#TODO: How to require user to be signed in for this?
@api_view(['GET'])
def get_all_saved_jobs(request):
    user_id = request.user.id
    saved_jobs = (SavedJob
                  .objects
                  .filter(user_id=user_id)
                  .values('job_id', company=F('job__company__name'), job_name=F('job__name'))
                  .annotate(avg_hourly_wage=Avg('job__salary__hourly_wage'), 
                            salary_count=Count('job__salary__id', distinct=True))
                  .annotate(avg_overall_rating=Avg('job__review__overall_rating'), 
                            review_count=Count('job__review__id', distinct=True)))
    
    saved_jobs_grouped_by_company = defaultdict(list)
    for job in saved_jobs:
        saved_jobs_grouped_by_company[job['company']].append(job)

    return Response(saved_jobs_grouped_by_company, status=status.HTTP_200_OK)

