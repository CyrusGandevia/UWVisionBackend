from os import stat
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .models import User
from rest_framework.authtoken.models import Token

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

# {
# "username": "cyrus-alt",
# "email": "cyrus.gandevia@gmail.com",
# "password": "cyrus12345"
# }

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

# {
# "username": "cyrus-alt",
# "password": "cyrus12345"
# }

# Email confirmation

# Nice-to-have: password reset

