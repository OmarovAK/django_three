from django.db import models
from django.urls import reverse


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date_pub = models.DateField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('library:list_books_for_date', args=[self.date_pub.year, self.date_pub.month, self.date_pub.day])
