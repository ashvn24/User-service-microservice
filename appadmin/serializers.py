from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class workSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extrakwargs = {
            "password":{"write_only":True}
        }