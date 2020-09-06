from django.shortcuts import render
from .models import *
from django.views.generic.list import ListView
from django.http import JsonResponse
from collections import OrderedDict
from django.views.decorators.csrf import csrf_exempt
#from django.utils.datastructures import SortedDict
def product_list(request):
    if request.method=="GET":
        request.session.modified = True
        #del request.session["cart"]
        objects = Product.objects.all()
        list1 = []
        if "cart" in request.session:
            for i in request.session["cart"]:
                list1.append(i["id"])
        return render(request,"products_list.html",{"productdata":objects,"list1":list1})
def add_product_to_cart(request,id):
    #print(request.session["cart"])
    pdata = Product.objects.get(id=id)
    data = OrderedDict()
    #data["id"] = id
    #data["qty"] = '1'
    #data["photo"] = pdata.photo
    #data["name"] = pdata.name



    #data["price"] = pdata.price
    #data["total"] = pdata.price
    #print(data)
    data = {"id":id,"photo":pdata.photo,"name":pdata.name,"price":pdata.price,"Quantity":1,"total":pdata.price}
    if "cart" not in request.session:
        request.session["cart"] = list()

    request.session["cart"].append(data)

    request.session.modified = True
    return JsonResponse({"status":"True","Message":"Cart Updated"})
@csrf_exempt
def remove_from_cart(request):
    id = request.POST["id"]
    del request.session['cart'][int(id)]
    request.session.modified = True
    return JsonResponse({"status":"True","Message":"Cart Updated"})
def show_cart(request):
    request.session.modified = True
    if "cart" in request.session:
        print(request.session["cart"])

    #request.session["cart"] = OrderedDict(sorted(request.session["cart"].items()))

    return render(request,"showcart.html")

def clear_cart(request):
    request.session.modified = True
    del request.session["cart"]
    return JsonResponse({"status":"True","Message":"Cart Cleared"})
@csrf_exempt
def increment(request):

    request.session.modified = True
    qty = request.POST["qty"];print("The quqntity is "+str(qty))
    id = request.POST["id"];print("The id is "+str(id))
    price = request.POST["price"];print(price)
    #item = request.POST["item"];print("The item is "+str(item))
    qty = int(qty) + 1
    total = qty * float(price)
    #request.session["cart"][str(id)]["qty"] = 0
    request.session["cart"][int(id)]["Quantity"] = str(qty)
    request.session["cart"][int(id)]["total"] = str(total)
    return JsonResponse({"status":"True","Qty":qty})

@csrf_exempt
def decrement(request):

    request.session.modified = True
    qty = request.POST["qty"];print("The quqntity is "+str(qty))
    id = request.POST["id"];print("The id is "+str(id))
    price = request.POST["price"]
    #item = request.POST["item"];print("The item is "+str(item))
    qty = int(qty) - 1
    total = qty * float(price)
    #request.session["cart"][str(id)]["qty"] = 0
    request.session["cart"][int(id)]["Quantity"] = str(qty)
    request.session["cart"][int(id)]["total"] = str(total)
    return JsonResponse({"status":"True","Qty":qty})