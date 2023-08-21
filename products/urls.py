from django.urls import path
from . import views

urlpatterns = [
    path('',views.show_products),
    path('category/',views.show_category),
    path('addCategory/',views.post_category),
    path('addProduct/',views.post_product),
]