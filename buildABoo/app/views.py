from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.


class Sec_Page(View):
    def get(self, request):
        return HttpResponse('This is the second page')
    
    
def home_page_view(request):
    return HttpResponse('This is the first page')

