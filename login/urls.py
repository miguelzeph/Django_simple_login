from django.urls import path

from .views import (
    login_page,
    register_page,
    home,
    home_admin,
    logout_page
    )

urlpatterns = [
    path('',home,name='home'),
    path('home_admin',home_admin,name='home_admin'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('register/', register_page, name='register')
]
