from django.shortcuts import render
from rest_framework import generics

from appadmin.producer import publish
from .serializers import *
from .models import *
from django.contrib.auth.models import User
# Create your views here.

class UserAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class WorkAPIView(generics.ListCreateAPIView):
    queryset = Work.objects.all()
    serializer_class = workSerializer
    
    def get_queryset(self):
        publish()
        return super().get_queryset()
    