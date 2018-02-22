# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    books = models.ManyToManyField(Book, related_name="authors")
    notes = models.TextField(null=True)

# Change the name of the 5th book to C#
# b = Book.objects.get(id=5)
# b.name = "C#"
# b.save()

# Change the first_name of the 5th author to Ketul
# c = Author.objects.last()
# c.first_name = "Ketul"
# c.save()

# Assign the first author to the first 2 books
# b = Author.objects.first()
# b.books.add(Book.objects.get(id=1))
# b.books.add(Book.objects.get(id=2))

# Assign the second author to the first 3 books
# Author.objects.get(id=2).books.add(Book.objects.get(id=1))
# Author.objects.get(id=2).books.add(Book.objects.get(id=2))
# Author.objects.get(id=2).books.add(Book.objects.get(id=3))

# Assign the third author to the first 4 books
# Author.objects.get(id=3).books.add(Book.objects.get(id=1))
# Author.objects.get(id=3).books.add(Book.objects.get(id=2))
# Author.objects.get(id=3).books.add(Book.objects.get(id=3))
# Author.objects.get(id=3).books.add(Book.objects.get(id=4))

# Assign the fourth author to the first 5 books (or in other words, all the books)
# Author.objects.get(id=4).books.add(Book.objects.get(id=1))
# Author.objects.get(id=4).books.add(Book.objects.get(id=2))
# Author.objects.get(id=4).books.add(Book.objects.get(id=3))
# Author.objects.get(id=4).books.add(Book.objects.get(id=4))
# Author.objects.get(id=4).books.add(Book.objects.get(id=5))

# For the 3rd book, retrieve all the authors
# Book.objects.get(id=3).authors.all()

# For the 3rd book, remove the first author
# Book.objects.get(id=3).authors.remove(Author.objects.get(id=2))

# For the 2nd book, add the 5th author as one of the authors
# Book.objects.get(id=2).authors.add(Author.objects.get(id=5))

# Find all the books that the 3rd author is part of
# Author.objects.get(id=3).books.all()

# Find all the books that the 2nd author is part of
# Author.objects.get(id=2).books.all()