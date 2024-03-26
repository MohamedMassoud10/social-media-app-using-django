from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
# Create your views here.
@login_required(login_url='signin')
def index(req):
    user_object = User.objects.get(username=req.user.username)
    user_profile = Profile.objects.get(user=user_object)
    return render(req,'index.html',{'WC':user_profile})

@login_required(login_url='signin')

def setting(req):
    print("the request: ",req)
    user_profile = Profile.objects.get(user=req.user)
    return render(req,'setting.html',{'user_profile':user_profile})



def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email is already registered!")
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.error(request, "Username is already taken!")
                return redirect('signup')
            else:
                # Create the user
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "Account created successfully!")

                # Authenticate the user and log them in
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                # Create a profile for the user
                profile = Profile.objects.create(user=user)
                profile.save()

                return redirect('settings')
        else:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')
    else:
        return render(request, 'signup.html')

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





def logout(req):
    auth.logout(req)
    return redirect('signin')