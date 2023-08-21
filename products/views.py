from django.shortcuts import render
from . models import Products,Category

# Create your views here.

def show_products(request):
    products = Products.objects.all()
    context= {
        "products": products
    }
    return render(request,"products/product-list.html",context)


def show_category(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request,"products/category-list.html",context)