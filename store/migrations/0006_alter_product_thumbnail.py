# Generated by Django 4.0.5 on 2022-06-19 14:23

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_product_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=store.models.image_Path),
        ),
    ]