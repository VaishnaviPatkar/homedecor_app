# Generated by Django 4.1.7 on 2023-03-22 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0003_rename_item_shape_item_item_brand'),
        ('userApp', '0002_remove_userinfo_id_alter_userinfo_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='myCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qyt', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminApp.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.userinfo')),
            ],
            options={
                'db_table': 'MyCart',
            },
        ),
    ]