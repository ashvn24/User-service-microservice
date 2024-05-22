from django.urls import path
from .views import *

urlpatterns = [
    path('reg/', UserAPIView.as_view()),
    path('work/', WorkAPIView.as_view()),
]
