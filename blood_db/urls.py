from django.conf.urls import patterns, include, url
from django.contrib import admin

 
urlpatterns = patterns('',
    url(r'', include('login.urls')),
    url(r'', include('api.urls')),
)


