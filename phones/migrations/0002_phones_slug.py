# Generated by Django 4.1.1 on 2022-09-25 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phones',
            name='slug',
            field=models.SlugField(default='hv'),
        ),
    ]
