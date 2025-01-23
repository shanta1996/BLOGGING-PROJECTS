from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *




# Create your views here.


def register_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method=='POST':
        fullname=request.POST['fullname']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        if password != cpassword:
            messages.add_message(request,messages.ERROR,'Password and confirm password did not matched.')
            return redirect('/register')
        else:
            user=User.objects.create_user(username=fullname,email=email,password=cpassword)
            user.full_name=fullname
            user.save()
            messages.add_message(request,messages.SUCCESS,'Your account has been created successfully.')
            return redirect('/login')

    return render(request,'accounts/register.html')

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method=='POST':
        fullname=request.POST['fullname']
        password=request.POST['password']

        user=authenticate(request,username=fullname,password=password)
        if user is not None: 
            login(request,user)
            # messages.add_message(request,messages.SUCCESS,'You have login successfully.')
            return redirect('/')
        else:
            messages.add_message(request,messages.ERROR,'Something went wrong')
            return redirect('login')
    return render(request,'accounts/login.html')

def logout_user(request):
    logout(request)
    return redirect('/')


# def profile(request):
#     if request.user.is_authenticated:
        
#         return render(request,'accounts/profile.html')
#     else:
#         return redirect('/login')
    


    
    
    
    

