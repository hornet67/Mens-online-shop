from django.shortcuts import render
import requests

from django.http import HttpResponse


# Create your views here.

def home(request):

    return render(request, 'home.html')

def formal_shirt(request):
    url = requests.get('https://fakestoreapi.com/products?sort=desc')
    data = url.json()
    return render(request,'Catagory/formal_shirt.html', {'data': data})


def cart(request):
    return render(request , 'cart.html')


def checkout(request):
    return render(request,'checkout.html')