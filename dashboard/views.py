from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the dashboard index.")

def staff(request):
    return HttpResponse("Hello, world. You're at the staff index.")