from django.shortcuts import render
from .models import Order


def order_list(request):
    data = Order.objects.filter(user=request.user)
    return render(request,'orders/order_list.html',{'orders':data})
# Create your views here.


def checkout(request):
    return render(request,'orders/checkout.html',{})