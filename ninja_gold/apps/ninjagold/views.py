# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import random, time

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['won'] = 0
        request.session['message'] = [] 
    return render(request, 'ninjagold/index.html')

def process(request):
    now = time.ctime()
    if request.POST['building'] == 'farm':
        request.session['won'] = random.randrange(10,21)
        activity = "Earned {} golds from the farm! ({})".format(request.session['won'], now)
    if request.POST['building'] == 'cave':
        request.session['won'] = random.randrange(5,11)
        activity = "Earned {} golds from the cave! ({})".format(request.session['won'], now)
    if request.POST['building'] == 'house':
        request.session['won'] = random.randrange(2,6)
        activity = "Earned {} golds from the house! ({})".format(request.session['won'], now)
    if request.POST['building'] == 'casino':
        request.session['won'] = random.randrange(-50,51)
        if request.session['won'] < 0:
            activity = "Entered a casino and lost {} golds... Ouch.. ({})".format(request.session['won'], now)
        else:
            activity = "Earned {} golds from the casino! ({})".format(request.session['won'], now)
    request.session['gold'] += request.session['won']
    request.session['message'].insert(0, activity)
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')