from django.urls import path
from .views import index, students, create_student, student_detail, update_student, delete_student

urlpatterns = [
    path('', index, name='index'),
    path('students/', students, name='students'),
    path('create/', create_student, name='create'),
    path('students/<int:pk>/', student_detail, name='detail'),
    path('edit/<int:pk>/', update_student, name='edit'),
    path('delete/<int:pk>/', delete_student, name='delete'),
]
