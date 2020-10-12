from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    recentorder = Order.objects.last()
    quantity_from_form = recentorder.quantity_ordered
    total_charge = recentorder.total_price
    orders = Order.objects.all()
    grandtotal = 0
    granditems = 0
    for i in orders:
        grandtotal += i.total_price
        granditems += i.quantity_ordered
    context = {
        "quantity" : quantity_from_form,
        "total" : total_charge,
        "grandtotal" : grandtotal,
        "granditems" : granditems
    }
    return render(request, "store/checkout.html",context)

def checkoutprocess(request):
    
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = Product.objects.get(id=request.POST["id"]).price
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    Order.objects.create(product = Product.objects.get(id=request.POST["id"]), quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect('/checkout')