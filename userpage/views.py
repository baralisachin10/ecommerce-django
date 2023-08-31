from django.shortcuts import render,redirect
from products.models import Products
from django.contrib.auth.decorators import login_required
from accounts.auth import user_only
from . models import Cart
from django.contrib import messages

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
    product = Products.objects.get(id=id)
    context={
        'product': product
    }
    return render(request,"client/product_details.html",context)

# function to add the items in the cart
@login_required
@user_only
def add_to_cart(request,product_id):
    user = request.user
    product= Products.objects.get(id = product_id)

    check_items_presence = Cart.objects.filter(user=user,product = product)

    if check_items_presence:
        messages.add_message(request,messages.ERROR,"Product already present in the cart")
        return redirect("/product")
    else:
        cart = Cart.objects.create(product=product, user=user)
        if cart:
            messages.add_message(request,messages.SUCCESS,"Item added to the cart")
            return redirect("/mycart")
        else:
            messages.add_message(request,messages.ERROR,"Unable to add item to the cart")
            return redirect("/product")


# function to show the cart items
@login_required
@user_only
def show_cart_items(request):
    user = request.user
    items = Cart.objects.filter(user=user)
    context = {
        'items': items
    }
    return render(request,"client/mycart.html",context)

