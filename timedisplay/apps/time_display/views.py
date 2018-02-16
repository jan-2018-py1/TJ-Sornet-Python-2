# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime
# Create your views here.
def index(request):
    context = {
        "date": strftime("%b %d, %Y", localtime()),
        "time": strftime("%H:%M %p", localtime())
    }
    return render(request, 'time_display/index.html', context)
