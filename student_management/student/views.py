from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Students
from .forms import StudentForm


def index(request):
    return render(request, 'index.html')


def students(request):
    students = Students.objects.all()
    context = {
        'students': students
    }

    return render(request, 'students.html', context=context)


def create_student(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            messages.success(request, 'Student has been created')
            return redirect('students')
    else:
        form = StudentForm()

    context = {
        'form': form
    }

    return render(request, 'form.html', context=context)


def student_detail(request, pk):
    student = Students.objects.get(id=pk)

    context = {
        "student": student,
    }

    return render(request, 'student_detail.html', context=context)


def update_student(request, pk):
    student = Students.objects.get(id=pk)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()

            return redirect('students')
    context = {
        "student": student,
        'form': form,
    }
    return render(request, 'form.html', context=context)


def delete_student(request, pk):
    student = Students.objects.get(id=pk)
    student.delete()

    return redirect('students')
