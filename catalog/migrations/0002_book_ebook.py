# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-16 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='ebook',
            field=models.FileField(default='ebook_XXX.pdf', upload_to='documents/'),
        ),
    ]
