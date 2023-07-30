from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['POST'])
def login(request):
    return Response({})

@api_view(['POST'])
def signup(request):
    return Response({})

@api_view(['GET'])
def test_token(request):
    return Response({})

class Sec_Page(View):
    def get(self, request):
        return HttpResponse('This is the second page')
    
    
def home_page_view(request):
    return HttpResponse('This is the first page')

