from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request,'home.html',{'name':'Rahul'})

def add(request):

    a = int(request.POST["num1"])
    b = int(request.POST["num2"])
    res = a + b

    return render(request,'result.html',{'result': res}) 
