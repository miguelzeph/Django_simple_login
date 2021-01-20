from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from .forms import CreatUserForm

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


def home(request):
    return render(request,'home.html')


def login_page(request):
    
    if request.method == "POST":
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password = password
            )
        
        if user is not None:
            

            login(request, user)
            messages.info(request,'VOCÊ JÁ ESTÁ LOGADO')
            return redirect('home')
        else:
            
            messages.info(request,'Username OR password is incorrect')


    return render(request,'login.html')





def register_page(request):
    #form = UserCreationForm()
    form = CreatUserForm()
    if request.method =="POST":
       #form = UserCreationForm(request.POST)
       form = CreatUserForm(request.POST)
       if form.is_valid():
           form.save()
           messages.success(request, 'Acount successfuly created')
           return redirect('login') # Depois que fizer o cadastro, vai para 
           #                        "name= login" que está na URLS.py

    context = {
        'form':form
    }
    return render(request,'register.html',context)