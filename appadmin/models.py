from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Work(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    salary = models.BigIntegerField()
    contact = models.BigIntegerField()
    Address = models.TextField()
    
    def __str__(self):
        return self.user
