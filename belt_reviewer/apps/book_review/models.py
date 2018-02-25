# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData["name"]) < 2:
            errors["name"] = "First Name Required; No fewer than 2 characters; letters only"
        if not postData['alias'].isalpha() or len(postData['alias']) < 2:
            errors["alias"] = "Last Name Required; No fewer than 2 characters; letters only"
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Email Required; Must be a valid format"
        if len(postData['password']) < 8: 
            errors["password"] = "Password Required; No fewer than 8 characters in length"
        if postData['password'] != postData['confirm']:
            errors["confirm"] = "Password must match"
        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="book_authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    review = models.TextField(null=True)
    rating = models.IntegerField()
    book = models.ForeignKey(Book, related_name="book_reviews")
    user = models.ForeignKey(User, related_name="user_reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserReview(models.Model):
    user = models.ForeignKey(User, related_name="books")
    book = models.ForeignKey(Book, related_name="users")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
