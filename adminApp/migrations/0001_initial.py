# Generated by Django 4.1.7 on 2023-03-12 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='item_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_category_name', models.CharField(max_length=50)),
                ('item_category_image', models.ImageField(default='abc.jpg', upload_to='images')),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('item_material', models.CharField(max_length=200)),
                ('item_colour', models.CharField(max_length=200)),
                ('item_shape', models.CharField(max_length=200)),
                ('item_price', models.FloatField(max_length=200)),
                ('item_dimension', models.CharField(max_length=200)),
                ('item_image', models.ImageField(default='abc.jpg', upload_to='images')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminApp.item_category')),
            ],
            options={
                'db_table': 'items',
            },
        ),
    ]
