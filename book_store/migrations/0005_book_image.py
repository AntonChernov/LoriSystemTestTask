# Generated by Django 3.1.1 on 2020-09-09 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0004_remove_book_rent_per_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, upload_to='book_store'),
        ),
    ]
