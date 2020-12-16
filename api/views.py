from django.shortcuts import render
from rest_framework import viewsets
from .serializer import StateSerializer
from restro_admin.models import StateModel
# Create your views here.

class StateModelViewset(viewsets.ModelViewSet):

    queryset = StateModel.objects.all()
    serializer_class = StateSerializer
    lookup_field = 'state_name'

