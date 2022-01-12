from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import UserRegistrationModel
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def home1(request):
    model1 = UserRegistrationModel.objects.all()
    template_name = 'app1/login1.html'
    context={'model1':model1}
    return render(request, template_name,context)

def home(request):
    model = UserRegistrationModel.objects.all()
    template_name = 'app1/base.html'
    context={'model':model}
    return render(request, template_name,context)
def registerView(request):
    form = UserRegistrationForm()
    if request.method=='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

            '''
            userObj = form.cleaned_data
            username = userObj['username']
            email = userObj['email']
            password = userObj['password']
            '''
            return HttpResponse('resister succefully')
    template_name='app1/resister.html'
    context ={'form':form}
    return render(request,template_name,context)

def loginView(request):

    if request.method =='POST':
        u =request.POST.get('username')
        p=request.POST.get('password')
        user = authenticate(username=u, passaword=p)
        if user is not None:
            login(request,user)

        else:
            messages.error(request,'invalid data enter')
        return redirect('home1')

    template_name='app1/login.html'
    context={}
    return render(request,template_name,context)

def logoutView(request):
    logout(request)
    return redirect('login')