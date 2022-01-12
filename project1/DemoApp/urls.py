from django.urls import path
from .views import registerView,home,loginView,logoutView,home1

urlpatterns = [
    path('',home,name='home'),
    path('login/',loginView, name='login'),
    path('home/',home1, name='home1'),
    path('logout/',logoutView, name='logout'),
    path('resister/',registerView, name='resister'),
]