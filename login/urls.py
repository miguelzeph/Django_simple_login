from django.urls import path

from .views import login_page,register_page,home,logout_page

urlpatterns = [
    path('',home,name='home'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('register/', register_page, name='register')
]
