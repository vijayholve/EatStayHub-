# Generated by Django 5.0.6 on 2024-06-14 10:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_alter_images_dish_alter_images_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='restaurant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.restaurants'),
        ),
    ]
