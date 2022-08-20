from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist

from .models import InterviewQuestion, UpvotedInterviewQuestion
from .serializers import InterviewQuestionSerializer, UpvotedInterviewQuestionSerializer

@api_view(['GET'])
@permission_classes([])
def get_all_interview_questions_for_job(request, **kwargs):
    # If job name is not passed
    job_id = kwargs.get('job_id', None)
    if not job_id:
        return Response({'error': 'No job id passed!'}, status=status.HTTP_400_BAD_REQUEST)

    # Find interview questions for current job 
    interview_questions = InterviewQuestion.objects.filter(job__id=job_id).values()

    # Fetch the upvoted interview questions for current job
    upvoted_interview_questions = UpvotedInterviewQuestion.objects.filter(interview_question__job_id=job_id)
    
    # Calculate number of upvotes per interview question
    upvoted_interview_questions_count = upvoted_interview_questions.values('interview_question_id').annotate(num_upvotes=Count('interview_question_id'))
    for interview_question in interview_questions:
        try:
            interview_question['num_upvotes'] = upvoted_interview_questions_count.get(interview_question_id=interview_question["id"])["num_upvotes"]
        except ObjectDoesNotExist:
            interview_question['num_upvotes'] = 0
        

    # If user is passed in authentication header, we also want to identify if the fetched questions have been upvoted
    if request.user.id:
        for interview_question in interview_questions:
                interview_question['upvoted'] = (upvoted_interview_questions
                                                    .filter(
                                                        interview_question_id=interview_question['id'],
                                                        user_id=request.user.id)
                                                    .exists())

    return Response(data=interview_questions, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_interview_question(request):
    # Create object from request payload
    data = {
            "job": request.data.get('job'), # primary key
            "body": request.data.get('body'),
            "year_worked": request.data.get('year_worked'),
            "term_worked": request.data.get('term_worked'),
            "coop_term_number": request.data.get('coop_term_number'),
            "program": request.data.get('program'),
            "added_by": request.user.id,
    }

    # Validate data against serializer
    serializer = InterviewQuestionSerializer(data=data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Create object
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def upvote_interview_question(request):
    # Create object from request payload
    data = {
        'interview_question': request.data.get('interview_question'), # primary key
        'user': request.user.id
    }
    
    # Validate data against serializer
    serializer = UpvotedInterviewQuestionSerializer(data=data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Upvote/un-Upvote Logic:
    upvoted_interview_question = UpvotedInterviewQuestion.objects.filter(interview_question=data['interview_question'], user=data['user'])
    # If interview question is already upvoted, we will un-upvote it
    if upvoted_interview_question: 
        upvoted_interview_question.delete()
        return Response({'response': 'removed upvote from interview question'}, status=status.HTTP_200_OK)
    else: # Otherwise, we save it
        serializer.save()
        return Response({'response': 'upvoted interview question'}, status=status.HTTP_201_CREATED)
