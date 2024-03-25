from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages
# Create your views here.

def index(req):
    return render(req,'index.html')


def signup(req):
    if req.method == 'POST':
        username = req.POST['username']
        email = req.POST['email']
        password = req.POST['password']
        password2 = req.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(req, "Email is already registered!")
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(req, "Username is already taken!")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(req, "Account created successfully!")
                return redirect('signin')
        else:
            messages.error(req, "Passwords do not match!")
            return redirect('signup')
    else:
        return render(req, 'signup.html')
def signin(req):
    return render(req,'signin.html')
