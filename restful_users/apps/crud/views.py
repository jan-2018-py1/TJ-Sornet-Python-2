# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from .models import Friend

# Create your views here.
def index(req):
    # query friends table
    # query = "SELECT * FROM friends"
    # all_users = mysql.query_db(query)
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
    # query = 'SELECT * FROM friends WHERE friends.id = :id'
    # data = {
    #     "id": id
    # }
    # getUser = mysql.query_db(query, data)[0]
    context = {
        "getUser": Friend.objects.get(id=id)
    }
    return render(req, 'crud/edit.html', context)

# GET /users/<id> - calls the show method to display the info for a particular user with given id. 
# This will need a template. - DONE
def show(req, id):
    # query = 'SELECT * FROM friends WHERE friends.id = :id'
    # data = {
    #     "id": id
    # }
    # getUser = mysql.query_db(query, data)[0]
    context = {
        "getUser": Friend.objects.get(id=id)
    }
    return render(req, 'crud/show.html', context)

# POST to /users/create - calls the create method to insert a new user record into our database. 
# This POST should be sent from the form on the page /users/new. Have this redirect to /users/<id> once created. - DONE
def create(req):
    # query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW());"
    # data = {
    #     "first_name": request.form['first_name'],
    #     "last_name": request.form['last_name'],
    #     "email": request.form['email'],
    # }
    # addUser = mysql.query_db(query, data)
    # print addUser
    addUser = Friend.objects.create(first_name=req.POST['first_name'], last_name=req.POST['last_name'], email=req.POST['email'])
    # return redirect(req, 'show', id=addUser))
    return redirect(req, 'users')

# GET /users/<id>/destroy - calls the destroy method to remove a particular user with the given id. 
# Have this redirect back to /users once deleted. - DONE
def destroy(req, id):
    # query = "DELETE FROM friends WHERE id = :id"
    # data = {
    #     "id": id
    # }
    # deleteUser = mysql.query_db(query, data)
    Friend.objects.get(id=id).delete()
    return redirect(reverse('crud_index'))

# POST /users/<id> - calls the update method to process the submitted form sent from /users/<id>/edit. 
# Have this redirect to /users/<id> once updated. - DONE
def update(req, id):
    # query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :id"
    # data = {
    #     "first_name": request.form['first_name'],
    #     "last_name": request.form['last_name'],
    #     "email": request.form['email'],
    #     "id": id
    # }
    # updateUser = mysql.query_db(query, data)
    b = Friend.objects.get(id=id)
    b.first_name = req.POST['first_name']
    b.last_name = req.POST['last_name']
    b.email = req.POST['email']
    b.save()
    url = "users/{}".format(id)
    # return redirect(req, 'crud_show', {'id':id})
    return redirect(req, url)

