from django.urls import path
from .views import index, students

urlpatterns = [
    path('', index, name='index'),
    path('students/', students, name='students'),
]
