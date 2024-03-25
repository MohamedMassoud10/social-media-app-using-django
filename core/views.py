from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(req):
    return render(req,'index.html')


def signup(req):
    return render(req,'signup.html')

def signin(req):
    return render(req,'signin.html')
