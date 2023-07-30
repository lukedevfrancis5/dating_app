from django.contrib import admin
from django.urls import path, include, re_path 
from app import views

urlpatterns = [
    path('home/', include('app.urls')),
    #path('profile/', include('app.urls')), for some reason this url bring you to the first page
    path('admin/', admin.site.urls),
    re_path('login', views.login),
    re_path('signup', views.signup),
    re_path('test_token', views.test_token),
    
]
