from django.shortcuts import render
from .models import Students

def index(request):
    return render(request, 'index.html')


def students(request):
    students = Students.objects.all()
    context = {
        'students': students
    }

    return render(request, 'students.html', context=context)


def create_student(request):
    pass


def student_detail(request):
    pass


def update_student(request):
    pass


def delete_student(request):
    pass
