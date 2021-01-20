from django.urls import path

from .views import login_page,register_page,home

urlpatterns = [
    path('',home,name='home'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register')
]
