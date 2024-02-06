# Generated by Django 5.0.2 on 2024-02-06 16:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('date_registration', models.DateField(default='2024-02-06')),
            ],
        ),
        migrations.CreateModel(
            name='GoodModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
                ('price_good', models.IntegerField(default=1)),
                ('quantity_good', models.IntegerField()),
                ('date_add', models.DateField(default='2024-02-06')),
            ],
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.IntegerField()),
                ('date', models.DateField(default='2024-02-06')),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lesson2.clientmodel')),
                ('id_good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lesson2.goodmodel')),
            ],
        ),
    ]