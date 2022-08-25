from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from django.db.models import Avg, Count, Func
from django.core.exceptions import ObjectDoesNotExist

from .models import Review, UpvotedReview
from .serializers import ReviewSerializer, UpvotedReviewSerializer

# Functionality for rounding to two decimal places for the Avg() functions
class Round(Func):
    function = "ROUND"
    template = "%(function)s(%(expressions)s::numeric, 2)"


@api_view(['GET'])
@permission_classes([]) 
def get_all_reviews_for_job(request, **kwargs): # Works very similar to 'get_all_interview_questions_for_job'
    # If job name is not passed
    job_id = kwargs.get('job_id', None)
    if not job_id:
        return Response({'error': 'No job id passed!'}, status=status.HTTP_400_BAD_REQUEST)

    # Find reviews for current job
    reviews = Review.objects.filter(job__id=job_id).values()

    # Fetch the upvoted reviews for current job
    upvoted_reviews = UpvotedReview.objects.filter(review__job_id=job_id)

    # Calculate number of upvotes per review
    upvoted_reviews_count = upvoted_reviews.values('review_id').annotate(num_upvotes=Count('review_id'))
    for review in reviews:
        try:
            review['num_upvotes'] = upvoted_reviews_count.get(review_id=review["id"])["num_upvotes"]
        except ObjectDoesNotExist:
            review['num_upvotes'] = 0
    
    # If user is passed in authentication header, we also want to identify if the fetched reviews have been upvoted
    if request.user.id:
        for review in reviews:
            review['upvoted'] = upvoted_reviews.filter(review_id=review['id'], user_id=request.user.id).exists()
    
    # Get overall rating for the job as well
    overall_review_rating = (
        reviews
        .aggregate(avg_work_life_balance_rating=Round(Avg('work_life_balance')),
                   avg_culture_rating=Round(Avg('culture')), 
                   avg_interesting_work_rating=Round(Avg('interesting_work')),
                   avg_overall_rating=Round(Avg('overall_rating')))
    )

    return Response(data={'overall_ratings': overall_review_rating, 'reviews': reviews}, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_review(request):
    # Create object from request payload
    data = {
            "job": request.data.get('job'),
            "body": request.data.get('body'),
            "work_life_balance": request.data.get('work_life_balance'),
            "culture": request.data.get('culture'),
            "interesting_work": request.data.get('interesting_work'),
            "overall_rating": request.data.get('overall_rating'),
            "year_worked": request.data.get('year_worked'),
            "term_worked": request.data.get('term_worked'),
            "coop_term_number": request.data.get('coop_term_number'),
            "program": request.data.get('program'),
            "added_by": request.user.id,
    }

    # Validate data against serializer
    serializer = ReviewSerializer(data=data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Create object
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def upvote_review(request):
    # Create object from request payload
    data = {
        'review': request.data.get('review'), # primary key
        'user': request.user.id
    }

    # Validate data against serializer
    serializer = UpvotedReviewSerializer(data=data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Upvote/un-Upvote Logic:
    upvoted_review = UpvotedReview.objects.filter(review=data['review'], user=data['user'])
    if upvoted_review: # If review is already upvoted, we will un-upvote it
        upvoted_review.delete()
        return Response({'response': 'removed upvote from review'}, status=status.HTTP_200_OK)
    else: # Otherwise, we upvote it
        serializer.save()
        return Response({'response': 'upvoted review'}, status=status.HTTP_201_CREATED)
