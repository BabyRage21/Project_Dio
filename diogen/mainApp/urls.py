from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),                                                                                                                                                                                                                                                                                                                                  
    path('', include('django.contrib.auth.urls')),
    #path('registration/', views.registration, name='registration'),
    #path('login/', views.login, name='login')

]
