from django.db import models
from django.urls import reverse


class Phones(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, default='hv')
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()

    def get_absolute_url(self):
        return reverse('phones:phones_detail', args=[self.slug])

    def __str__(self):
        return self.name
