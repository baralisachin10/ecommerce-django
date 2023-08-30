from django.shortcuts import render
from products.models import Products
# Create your views here.

def home_page(request):
    products = Products.objects.all().order_by('-id')[:8]
    context = {
        'products': products
    }
    return render(request,"client/homepage.html",context)

def product_page(request):
    products = Products.objects.all()
    context = {
        'products':products
    }
    return render(request,"client/productpage.html",context)

def product_details_page(request,id):
    single_product = Products.objects.get(id=id)
    context={
        'single_product': single_product
    }
    return render(request,"client/product_details.html",context)
