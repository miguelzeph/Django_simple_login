from django.http import HttpResponse
from django.shortcuts import redirect,render



# Este decorator mostra que se você está autenticado, não há
# necessidade de entrar nesta página (login/register por exemplo)...
# Então, quando você tentar ela redireciona pra home, bem interessante!!!
def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_function(request,*args,**kwargs):
            group = None

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request,*args,**kwargs)
            else:
                return render(request,'nao_autorizado.html')
        return wrapper_function
    return decorator

def admin_only(view_func):
    def wrapper_function(request,*args,**kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == "customer":
            #return redirect('home')
            return render(request,'nao_autorizado.html')
        if group == "admin":
            return view_func(request,*args,**kwargs)
    
    return wrapper_function
