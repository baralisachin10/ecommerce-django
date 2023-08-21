from django.urls import path
from . import views

urlpatterns = [
    path('',views.show_products),
    path('category/',views.show_category),
]