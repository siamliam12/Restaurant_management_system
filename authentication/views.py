from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny

import requests
from .serializers import CreateUserSerializer

CLIENT_ID = '<client_id>'
CLIENT_SECRET = '<client_secret>'

@api_view(['POST'])
@permission_classes([AllowAny])
def register():
    pass