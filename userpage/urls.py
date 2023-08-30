from django.urls import path

from . import views

urlpatterns = [
    path('',views.home_page, name="homepage"),
    path('product/',views.product_page , name = "productpage"),
    path('product/<int:id>',views.product_details_page,name="product_detail")
]