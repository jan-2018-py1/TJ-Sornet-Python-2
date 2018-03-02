# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import *
import md5

# Create your views here.
def index(req):
    if "user_id" in req.session:
        return redirect('/books')
    return render(req, 'book_review/index.html')

def login(req):
    user = User.objects.filter(email=req.POST['email'])
    if user:
        current_user = user[0]
        if current_user.password == md5.new(req.POST['password']).hexdigest():
            req.session['user_id'] = current_user.id
            return redirect('/books')
    messages.error(req, "No email and password combo found")
    return redirect('/')

def register(req):
    errors = User.objects.basic_validator(req.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(req, error, extra_tags=tag)
        return redirect('/')
    else:
        user = User.objects.create(name=req.POST['name'], alias=req.POST['alias'], email=req.POST['email'], password=md5.new(req.POST['password']).hexdigest())
        req.session["user_id"] = user.id
        return redirect('/books')

def logout(req):
	del req.session['user_id']
	return redirect("/")

def books(req):
    context = {
        "user": User.objects.get(id=req.session['user_id']),
        "review": Review.objects.all().order_by('-created_at'),
        "book": Book.objects.all()
    }
    return render(req, 'book_review/bookreview.html', context)

def add(req):
    context = {
        "authors": Author.objects.all()
    }
    return render(req, 'book_review/add.html', context)

def create(req):
    if req.POST['new_author'] == "":
        auth = Author.objects.get(name=req.POST['author'])
        auth_id = auth.id
    else:
        auth = Author.objects.create(name=req.POST['new_author'])
        auth_id = auth.id
    book = Book.objects.create(title=req.POST['title'], author=auth)
    book_id = book.id
    user = User.objects.get(id=req.session['user_id'])
    review = Review.objects.create(review=req.POST['review'], rating=int(req.POST['rating']), book=book, user=user)
    review_id = review.id
    return HttpResponseRedirect(reverse('book_show', kwargs={'id':book_id}))

def show_book(req, id):
    context = {
        "book": Book.objects.get(id=id),
        "review": Review.objects.filter(book = Book.objects.get(id=id))
    }
    return render(req, 'book_review/book.html', context)

def show_user(req, id):
    context = {
        "user": User.objects.get(id=id),
        "review": Review.objects.filter(user = User.objects.get(id=id))
    }
    return render(req, 'book_review/user.html', context)

def addreview(req):
    book_id = req.POST['book_id']
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=req.session['user_id'])
    review = Review.objects.create(review=req.POST['review'], rating=int(req.POST['rating']), book=book, user=user)
    review_id = review.id
    return HttpResponseRedirect(reverse('book_show', kwargs={'id':book_id}))
# def destroy(req, id):
#     return HttpResponseRedirect(reverse('book_show', kwargs={'id':user_id}))
