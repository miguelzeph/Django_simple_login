from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from .forms import CreatUserForm

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


from django.contrib.auth.decorators import login_required


# Meu pŕoprio Decorator
from .decorators import unauthenticated_user


# Restringe as Url que você pode entrar sem 
# estar logado
@login_required(login_url='login') 
def home(request):
    #print(request.user.is_authenticated) #False ou True
    return render(request,'home.html')

@unauthenticated_user
def login_page(request):
    
    if request.method == "POST":
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username= username,
            password = password
            )
        
        if user is not None:
            

            login(request, user)
            messages.info(request,'VOCÊ JÁ ESTÁ LOGADO')
            return redirect('home')
        else:
            
            messages.info(request,'Username OR password is incorrect')

    
    """       FIZ O MEU DECORATOR
    # Não deixa entrar na Página de Login se você já estiver Logado
    # Não dá para usar o Decorator de @login_required aqui...
    if request.method == "GET" and request.user.is_authenticated == True:
        return redirect('home')
    """
    



    return render(request,'login.html')


@unauthenticated_user
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


    """       FIZ O MEU DECORATOR
    # Não deixa entrar na Página de Login se você já estiver Logado
    # Não dá para usar o Decorator de @login_required aqui...
    if request.method == "GET" and request.user.is_authenticated == True:
        return redirect('home')
    """


    return render(request,'register.html',context)

# Restringe as Url que você pode entrar sem 
# estar logado
@login_required(login_url='login') 
def logout_page(request):
    logout(request)
    return redirect('login')