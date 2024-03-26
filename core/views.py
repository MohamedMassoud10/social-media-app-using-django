from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
# Create your views here.
@login_required(login_url='signin')
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

                #log user in an redirect to the settings page

                #create a profile object for the new user 
                user_model =User.objects.get(username=username)
                new_profile=Profile.objects.create(user=user_model)
                new_profile.save()
                return redirect('signup')

        else:
            messages.error(req, "Passwords do not match!")
            return redirect('signup')
    else:
        return render(req, 'signup.html')


def signin(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(req, user)
            return redirect('/')
        else:
            messages.info(req, 'Credentials Invalid')
            return redirect('signin')

    else:
        return render(req, 'signin.html')


def setting(req):
    return render(req,'setting.html',)


def logout(req):
    auth.logout(req)
    return redirect('signin')