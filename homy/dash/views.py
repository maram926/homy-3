from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth import authenticate, login, logout # type: ignore
from django.contrib.auth.forms import AuthenticationForm # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from .forms import LoginForm 
from .forms import SinupForm
from django.views.decorators.cache import never_cache # type: ignore



def home(request):
    return render(request,'dash/home.html')


def logout_view(request):
    logout(request)
    return render(request , 'dash/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Log the user in
            login(request, user)
            # Redirect to a home page after successful login
            return render(request, 'dash/home.html')  
    else:
        form = LoginForm()  # Show an empty form on a GET request

    # Render the login page with the form, showing any errors if form is invalid
    return render(request, 'dash/login.html', {'form': form})
       





def signup_view(request):
    if request.method == 'POST':
        form = SinupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request , 'dash/home.html') 
    else:
        form = SinupForm()
    return render(request,'dash/singup.html' , {'form':form})