from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate

from .models import User

# NOTE: User signup/login APIs are still undergoing migration from old service

# Create User (sign up)
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create_user(request):
    user = User.objects.create_user(
        request.data.get('username'),
        request.data.get('email'),
        request.data.get('password'),
    )

    # TODO: Future - add serialization and error handling
    return Response({'response': 'user created!'}, status=status.HTTP_201_CREATED)


# Log In -> returns credentials + token
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def get_user(request):
    user = authenticate(
        username=request.data.get('username'),
        password=request.data.get('password')
    )
    
    if not user:
        return Response({'response': 'Incorrect user credentials'}, status=status.HTTP_404_NOT_FOUND)

    # Return username, email and token
    credentials = {
        "username": user.get_username(),
        "email": user.email,
        "token": Token.objects.get(user=user).key
    }
    
    return Response(data=credentials, status=status.HTTP_200_OK)

# TODO: Email confirmation

# TODO: Password reset