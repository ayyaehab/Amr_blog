# Generated by Django 4.0.3 on 2022-05-30 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('description', models.TextField(max_length=3000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('oldPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('img', models.ImageField(default=True, upload_to='static/imgs/book')),
                ('productCondition', models.CharField(max_length=45)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LapTop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('description', models.TextField(max_length=3000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('oldPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('brand', models.CharField(max_length=20)),
                ('product_information', models.TextField(max_length=3000)),
                ('productCondition', models.CharField(max_length=45)),
                ('thumbnail', models.ImageField(default=True, upload_to='static/imgs/laptop')),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('description', models.TextField(max_length=3000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('oldPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('color', models.CharField(max_length=20)),
                ('productCondition', models.CharField(max_length=45)),
                ('thumbnail', models.ImageField(default=True, upload_to='static/imgs/mug')),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('description', models.TextField(max_length=3000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('oldPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('brand', models.CharField(max_length=20)),
                ('product_information', models.TextField(max_length=3000)),
                ('productCondition', models.CharField(max_length=45)),
                ('thumbnail', models.ImageField(default=True, upload_to='static/imgs/pc')),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tshirt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('description', models.TextField(max_length=3000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('oldPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('color', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=20)),
                ('product_information', models.TextField(max_length=3000)),
                ('productCondition', models.CharField(max_length=45)),
                ('thumbnail', models.ImageField(default=True, upload_to='static/imgs/shirt')),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TshirtImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default=True, upload_to='static/imgs/shirt')),
                ('tshirt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.tshirt')),
            ],
        ),
        migrations.CreateModel(
            name='PcImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default=True, upload_to='static/imgs/pc')),
                ('pc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.pc')),
            ],
        ),
        migrations.CreateModel(
            name='MugImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default=True, upload_to='static/imgs/mug')),
                ('mug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.mug')),
            ],
        ),
        migrations.CreateModel(
            name='LapTopImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default=True, upload_to='static/imgs/laptop')),
                ('lapTop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.laptop')),
            ],
        ),
    ]
