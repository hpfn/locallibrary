# Generated by Django 2.0.7 on 2018-07-30 17:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_book_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ('last_name',)},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('title',)},
        ),
        migrations.AlterField(
            model_name='book',
            name='ebook',
            field=models.FileField(default='ebook_XXX.pdf', upload_to='documents/', validators=[django.core.validators.FileExtensionValidator(['pdf'], 'Apenas arquivos PDF')]),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default='ebook_img.jpeg', upload_to='img/'),
        ),
    ]
