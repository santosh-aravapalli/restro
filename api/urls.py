from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import StateModelViewset

api_urls = DefaultRouter()
api_urls.register('state',StateModelViewset)


urlpatterns = [

    path('',include(api_urls.urls)),

]
