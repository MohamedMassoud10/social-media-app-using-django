from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile,Post,Comment
# Create your views here.
@login_required(login_url='signin')
def index(req):
    user_object = User.objects.get(username=req.user.username)
    user_profile = Profile.objects.get(user=user_object)
    posts=Post.objects.all()
    return render(req,'index.html',{'user_profile':user_profile,'posts':posts})


def upload(req):
    if req.method=="POST":
        user=req.user.username
        image=req.FILES.get('image_upload') # image_upload is the name of 'name' attribute in the HTML structure  
        caption=req.POST['caption']
        new_post=Post.objects.create(user=user,image=image,caption=caption)
        new_post.save()
        redirect('/')
    else:
        redirect('/')



@login_required(login_url='signin')
def setting(req):
    user_profile = Profile.objects.get(user=req.user)

    if req.method == 'POST':
        if req.FILES.get('image')==None:
            image=user_profile.profileimag
            bio = req.POST['bio']
            location = req.POST['location']

            user_profile.profileimag=image
            user_profile.bio=bio
            user_profile.location=location
            user_profile.save()
        if req.FILES.get('image') != None :
            image=req.FILES.get('image')
            bio = req.POST['bio']
            location = req.POST['location']

            user_profile.profileimag=image
            user_profile.bio=bio
            user_profile.location=location
            user_profile.save()    
    
    return render(req,'setting.html',{'user_profile':user_profile})

@login_required(login_url='signin')
def add_comment(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        comment_text = request.POST.get('comment_text')
        post = Post.objects.get(id=post_id)
        user = request.user
        comment = Comment.objects.create(post=post, user=user, text=comment_text)
        comment.save()
    return redirect('index')

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