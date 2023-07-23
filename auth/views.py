from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
# Create your views here.

def home(request):
    return render(request,"auth/index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2') 

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your account has been successfully created")
        return redirect(signin)

    return render(request,"auth/signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            fname=user.fname
            return render(request,'authentication/index.html',{'fname':fname})

        else:
            messages.error(request,"Bad Credentials")
            return redirect('home')
    return render(request,"auth/signin.html")

def signout(request):
    pass

