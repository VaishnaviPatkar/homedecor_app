# Generated by Django 4.1.7 on 2023-03-20 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='id',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='userName',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]