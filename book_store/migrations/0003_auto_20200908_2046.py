# Generated by Django 3.1.1 on 2020-09-08 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0002_auto_20200908_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(editable=False, unique=True),
        ),
    ]
