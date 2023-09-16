from django.shortcuts import render,redirect
from .form import RegistrationForm
from django.contrib.auth import authenticate,login,logout

import requests



# Create your views here.

def home(request):

    return render(request, 'home.html')


def formal_shirt(request):
    url = requests.get('https://fakestoreapi.com/products?sort=desc')
    data = url.json()
    return render(request, 'Catagory/formal_shirt.html', {'data': data})


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')


def login_page(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)
        print("User:", user)
        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request, 'user/Login.html')


def signup_page(request):
    if request.method == 'POST':
        forms = RegistrationForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('login')

    forms = RegistrationForm()

    return render(request, 'user/signup.html', {'forms': forms})



