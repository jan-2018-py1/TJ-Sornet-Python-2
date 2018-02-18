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

def result(request):
    context = {
        "name": request.POST['name'],
        "location": request.POST['place'],
        "language": request.POST['language'],
        "comment": request.POST['comment']
    }
    
    return render(request, 'survey/results.html', context)
