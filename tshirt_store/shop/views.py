from django.shortcuts import render
from .models import TShirt

# Create your views here.


def index(request):
    return render(request, 'shop/index.html', {'tshirts': TShirt.objects.all()})


def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')

def products(request):
    tshirts = TShirt.objects.all()
    return render(request, 'shop/products.html', {'tshirts': tshirts})