# Generated by Django 4.0.5 on 2022-06-17 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_thumbnail1_product_thumbnail2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
    ]