from django.shortcuts import render
from products.models import Products
# Create your views here.

def home_page(request):
    products = Products.objects.all().order_by('-id')[:8]
    context = {
        'products': products
    }
    return render(request,"client/homepage.html",context)
