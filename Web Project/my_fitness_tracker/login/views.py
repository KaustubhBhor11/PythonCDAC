from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request,'login.html')
