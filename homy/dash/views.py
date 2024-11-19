from django.shortcuts import render, redirect , get_object_or_404# type: ignore
from django.contrib.auth import authenticate, login, logout # type: ignore
from django.contrib.auth.forms import AuthenticationForm # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from .forms import LoginForm 
from .forms import SinupForm
from django.views.decorators.cache import never_cache # type: ignore
from .models import ChefOffering , Dish



def home(request):
    chef_offerings = ChefOffering.objects.all()
    return render(request,'dash/home.html' , {'chef_offerings': chef_offerings})


def logout_view(request):
    chef_offerings = ChefOffering.objects.all()
    logout(request)
    return render(request , 'dash/home.html' , {'chef_offerings': chef_offerings})

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



def chef(request):
    category = request.GET.get('category')  # Get category from query string
    search_query = request.GET.get('search')
    if category:
        chef_offerings = ChefOffering.objects.filter(category=category)
    else:
        chef_offerings = ChefOffering.objects.all()
    if search_query:
        chef_offerings = chef_offerings.filter(name__icontains=search_query)    
    return render(request, 'dash/chef.html', {'chef_offerings': chef_offerings})
  





def menu2(request, offering_id):
    offering = get_object_or_404(ChefOffering, id=offering_id)
    dishes = offering.dishes.all()
    return render(request, 'dash/menu2.html', {
        'offering': offering,
        'dishes': dishes
    })


def singleDish(request , singleDish_id):
    dish = get_object_or_404(Dish, id=singleDish_id)
    return render(request,'dash/singleDish.html', {'dish': dish})

def cart(request):
    return render(request,'dash/cart.html')


def order(request):
    return render(request,'dash/order.html')

@login_required
def profile(request):
    return render(request, 'dash/profile.html', {'user': request.user})