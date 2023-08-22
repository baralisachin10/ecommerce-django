from django.shortcuts import render
from . models import Products

# Create your views here.

def show_products(request):
    products = Products.objects.all()
    context= {
        "products": products
    }
    return render(request,"products/product-list.html",context)
