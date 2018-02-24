# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Friend

# Create your views here.
def index(req):
    context = {
        "all_users": Friend.objects.all()
    }
    return render(req, 'crud/index.html', context)

# GET request to /users/new - calls the new method to display a form allowing users to create a new user. 
# This will need a template. - DONE
def new(req):
    return render(req, 'crud/new.html')

# GET request /users/<id>/edit - calls the edit method to display a form allowing users to 
# edit an existing user with the given id. This will need a template. - DONE
def edit(req, id):
    context = {
        "getUser": Friend.objects.get(id=id)
    }
    return render(req, 'crud/edit.html', context)

# GET /users/<id> - calls the show method to display the info for a particular user with given id. 
# This will need a template. - DONE
def show(req, id):
    context = {
        "getUser": Friend.objects.get(id=id)
    }
    return render(req, 'crud/show.html', context)

# POST to /users/create - calls the create method to insert a new user record into our database. 
# This POST should be sent from the form on the page /users/new. Have this redirect to /users/<id> once created. - DONE
def create(req):
    addUser = Friend.objects.create(first_name=req.POST['first_name'], last_name=req.POST['last_name'], email=req.POST['email'])
    user_id = addUser.id
    return HttpResponseRedirect(reverse('crud_show', kwargs={'id':user_id}))

# GET /users/<id>/destroy - calls the destroy method to remove a particular user with the given id. 
# Have this redirect back to /users once deleted. - DONE
def destroy(req, id):
    Friend.objects.get(id=id).delete()
    return redirect(reverse('crud_index'))

# POST /users/<id> - calls the update method to process the submitted form sent from /users/<id>/edit. 
# Have this redirect to /users/<id> once updated. - DONE
def update(req):
    user_id = req.POST['id']
    b = Friend.objects.get(id=user_id)
    b.first_name = req.POST['first_name']
    b.last_name = req.POST['last_name']
    b.email = req.POST['email']
    b.save()
    return HttpResponseRedirect(reverse('crud_show', kwargs={'id':user_id}))
    

