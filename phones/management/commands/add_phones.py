import csv
import os
from phones.models import Phones
from slugify import slugify
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        file = os.path.join(os.getcwd(), 'phones.csv')
        with open(file, encoding='utf-8') as f:
            file_reader = csv.DictReader(f, delimiter=";")
            list_id = [i.id for i in Phones.objects.all()]
            for i in file_reader:
                if int(i['id']) not in list_id:
                    slug_name = slugify(i['name'])
                    Phones.objects.create(id=i['id'], name=i['name'], price=i['price'], release_date=i['release_date'],
                                          lte_exists=i['lte_exists'], image=i['image'], slug=slug_name)
