from django.shortcuts import render
from .models import Student


from django.http import HttpResponse

def home(request):
    return render(request, 'app1/home.html')



def show_students(request):
    students = Student.objects.all()
    return render(request, 'app1/show.html', {'students': students})


def about(request):
    return render(request, 'app1/about.html')
