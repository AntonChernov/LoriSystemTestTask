# Generated by Django 3.1.1 on 2020-09-08 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(default='', editable=False),
        ),
    ]