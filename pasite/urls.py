from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    
    url(r'^route/', include('routefinder.urls', namespace='route')),

]

