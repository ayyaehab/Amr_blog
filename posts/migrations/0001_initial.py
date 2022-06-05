# Generated by Django 4.0.3 on 2022-06-03 14:52

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('overview', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('thumbnail', models.ImageField(default=True, upload_to='static/imgs/posts')),
                ('smalltitle', models.CharField(max_length=80)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
    ]
