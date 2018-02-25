# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
import md5

def index(req):
	if "user_id" in req.session:
		return redirect('/success')
	return render(req, "login_reg/index.html")

def success(req):
	data = {
		"user": User.objects.get(id=req.session['user_id'])
	}
	return render(req, 'login_reg/success.html', data)


def login(req):
    user = User.objects.filter(email=req.POST['email'])
    if user:
        current_user = user[0]
        if current_user.password == md5.new(req.POST['password']).hexdigest():
            req.session['user_id'] = current_user.id
            return redirect('/success')
    messages.error(req, "No email and password combo found")
    return redirect('/')

def register(req):
    errors = User.objects.basic_validator(req.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(req, error, extra_tags=tag)
        return redirect('/')
    else:
        user = User.objects.create(first_name=req.POST['first_name'], last_name=req.POST['last_name'], email=req.POST['email'], password=md5.new(req.POST['password']).hexdigest())
        req.session["user_id"] = user.id
        return redirect('/success')

def logout(req):
	del req.session['user_id']
	return redirect("/")