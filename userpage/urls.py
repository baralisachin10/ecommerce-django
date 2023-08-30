from django.urls import path

from . import views

urlpatterns = [
    path('',views.home_page, name="homepage"),
    path('product/',views.product_page , name = "productpage"),
]