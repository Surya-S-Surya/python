from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'add.html')
def add(request):
    n1=int(request.GET['mark1'])
    n2=int(request.GET['mark2'])
    Name=request.GET['name']
    Reg=request.GET['regno']
    res=n1+n2
    return HttpResponse('Finished')
