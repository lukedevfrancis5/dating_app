from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status 
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


# Create your views here.

@api_view(['POST'])
def login(request):
    return Response({})

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, "user":serializer.data})
    return Response({})

@api_view(['GET'])
def test_token(request):
    return Response({})

class Sec_Page(View):
    def get(self, request):
        return HttpResponse('This is the second page')
    
    
def home_page_view(request):
    return HttpResponse('This is the first page')

