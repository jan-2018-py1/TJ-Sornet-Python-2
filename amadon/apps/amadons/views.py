# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return redirect('/amadon')

def amadon(request):
    return render(request, 'amadons/index.html')

def buy(request):
    if 'quantity' not in request.session:
        request.session['quantity'] = 0
    pricing = {
        "1010": 19.99,
        "1011": 29.99,
        "1012": 4.99,
        "1013": 49.99,
    }
    price = 0
    for prod_id, val in pricing.items():
        if request.POST['product_id'] == prod_id:
            price = val
    purchase_price = price * int(request.POST['quantity'])
    request.session['purchase_price'] = purchase_price
    request.session['totalPrice'] += purchase_price
    request.session['quantity'] += int(request.POST['quantity'])
    return redirect('/amadon/checkout')

def checkout(request):
    return render(request, 'amadons/checkout.html')

def clear(request):
    request.session['quantity'] = 0
    request.session['totalPrice'] = 0
    return redirect ('/')