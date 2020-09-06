from django.urls import path,include
from .views import *
urlpatterns = [

    path('allproducts',product_list,name="allproducts"),
    path("showcart",show_cart,name="showcart"),
    path("clearcart",clear_cart,name="clearcart"),
    path("addtocart/<int:id>",add_product_to_cart,name="addtocart"),
    path("removefromcart",remove_from_cart,name="removefromcart"),
    path("increment",increment,name="increment"),
    path("decrement",decrement,name="decrement"),

]
