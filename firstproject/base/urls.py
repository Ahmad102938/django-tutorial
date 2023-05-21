from django.contrib import admin
from django.urls import path
from base import views


urlpatterns = [ 
    path('', views.home),
    path('hello-world/', views.helloworld),
    path('hello-world/<int:helloid>', views.innerhello),
    path('hello-world/<allid>', views.allhello),
    path('about-us/', views.aboutus),
    path('services/', views.services, name="services")
]
