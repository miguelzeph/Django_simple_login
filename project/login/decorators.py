from django.http import HttpResponse
from django.shortcuts import redirect



# Este decorator mostra que se você está autenticado, não há
# necessidade de entrar nesta página... logo, por exemplo, 
# se você está logado, por que quer entrar na página /login/ ou register/ ???

# Então, quando você tentar ela redireciona pra home, bem interessante!!!

def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func