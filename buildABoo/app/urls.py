from django.urls import path 
from . import views
from .views import Sec_Page

urlpatterns = [
    path('', views.home_page_view),
    path('profile', Sec_Page.as_view())
]