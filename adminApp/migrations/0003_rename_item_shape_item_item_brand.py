# Generated by Django 4.1.7 on 2023-03-15 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0002_rename_item_image_item_item_image1_item_item_image2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item_shape',
            new_name='item_brand',
        ),
    ]
