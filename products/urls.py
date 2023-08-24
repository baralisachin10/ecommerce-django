from django.urls import path
from . import views

urlpatterns = [
    path('',views.show_products),
    path('category/',views.show_category),
    path('addCategory/',views.post_category),
    path('addProduct/',views.post_product),
    path('deleteCategory/<int:category_id>',views.delete_category, name="delete_category"),
    path('updateCategory/<int:category_id>',views.update_category, name= 'update_category'),
    path('deleteProduct/<int:product_id>',views.delete_product, name="delete_product"),
    path('updateProduct/<int:product_id>',views.update_product,name = "update_product"),
]