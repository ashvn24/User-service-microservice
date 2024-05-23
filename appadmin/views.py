from django.shortcuts import render
from rest_framework import generics

from appadmin.producer import RabbitMQProducer
from .serializers import *
from .models import *
from django.contrib.auth.models import User
# Create your views here.

class UserAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def perform_create(self, serializer):
        user = serializer.save()
        user_detail = {
            'content': f'New account has been created for user, {user.email}',
            'type': 'Registration'
        }
        producer = RabbitMQProducer()
        producer.publish('new user registered', user_detail)
        return super().perform_create(serializer)
    
class WorkAPIView(generics.ListCreateAPIView):
    queryset = Work.objects.all()
    serializer_class = workSerializer
    
    
    