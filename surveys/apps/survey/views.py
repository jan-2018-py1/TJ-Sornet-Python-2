# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] += 1
    return render(request, 'survey/index.html')

def process(request):
    if 'counter' not in request.session:
        request.session['counter'] = 1
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['place']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('/result')
    
def result(request):
    return render(request, 'survey/results.html')
