from django.shortcuts import render, redirect
from .models import Products, Category
from .forms import CategoryForm, ProductForm
from django.contrib import messages

# Create your views here.


# function to show products
def show_products(request):
    products = Products.objects.all()
    context = {"products": products}
    return render(request, "products/product-list.html", context)


# function to show category
def show_category(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "products/category-list.html", context)


# function to add category using form
def post_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS, "Category added successfully!"
            )
            return redirect("/products/category")
        else:
            messages.add_message(request, messages.ERROR, "Failed to add Category!")
            return render(request, "products/addCategory.html", {"form": CategoryForm})

    context = {"form": CategoryForm}
    return render(request, "products/addCategory.html", context)


# function to add product using form
def post_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS, "Product added successfully!"
            )
            return redirect("/products/")
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Failed to add product, please verify the form field",
            )
            return render(request, "products/addProduct.html", {"form": ProductForm})
    context = {"form": ProductForm}
    return render(request, "products/addProduct.html", context)


# to delete the category


def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    messages.add_message(request, messages.SUCCESS, "Category deleted successfully")
    return redirect("/products/category")


# to update the category using category form
def update_category(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS, "Category updated successfully!"
            )
            return redirect("/products/category")
        else:
            messages.add_message(request, messages.ERROR, "Failed to update category!")
            return render(request, "products/addCategory.html", {"form": form})
    context = {"form": CategoryForm(instance=category)}
    return render(request, "products/addCategory.html", context)


# to delete the product


def delete_product(request, product_id):
    products = Products.objects.get(id=product_id)
    products.delete()
    messages.add_message(request, messages.SUCCESS, "Product deleted successfully")
    return redirect("/products/")


# to update product using productForm


def update_product(request, product_id):
    product = Products.objects.get(id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS, "Product updated successfully"
            )
            return redirect("/products/")
        else:
            messages.add_message(request, messages.ERROR, "Failed to update products")
            return render(request, "products/addProduct.html", {"form": form})
    context = {"form": ProductForm(instance=product)}
    return render(request, "products/addProduct.html", context)
