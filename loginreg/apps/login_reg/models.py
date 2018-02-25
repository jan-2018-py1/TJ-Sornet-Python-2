# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if not postData['first_name'].isalpha() or len(postData["first_name"]) < 2:
            errors["firstname"] = "First Name Required; No fewer than 2 characters; letters only"
        if not postData['last_name'].isalpha() or len(postData['last_name']) < 2:
            errors["lastname"] = "Last Name Required; No fewer than 2 characters; letters only"
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Email Required; Must be a valid format"
        if len(postData['password']) < 8: 
            errors["password"] = "Password Required; No fewer than 8 characters in length"
        if postData['password'] != postData['confirm']:
            errors["confirm"] = "Password must match"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
