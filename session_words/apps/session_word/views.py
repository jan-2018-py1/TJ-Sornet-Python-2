# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from time import localtime, strftime

# Create your views here.
def index(request):
    return redirect ('/session_words')

def session(request):
    if 'word_list' not in request.session:
        list_word = []
        request.session['word_list'] = list_word
    return render (request, 'session_word/index.html')

def add_word(request):
    if request.method == "POST":
        new_word_list = {
            "word": request.POST['new_word'],
            "color": request.POST['color'],
            "size": request.POST['sizeChoice'],
            "time": strftime("%H:%M:%S %p, %b %d %Y", localtime())
        }
        print new_word_list
        temp_list = request.session['word_list']
        temp_list.append(new_word_list)
        request.session['word_list'] = temp_list
        print request.session['word_list']
    return redirect ('/')

def clear(request):
    list_word = []
    request.session['word_list'] = list_word
    return redirect ('/')