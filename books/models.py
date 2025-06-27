from django.db import models
from django.db.models import BooleanField
from django.forms import CharField


class LibraryBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ['author']

    def __str__(self):
        return f"{self.title} by {self.author}"
