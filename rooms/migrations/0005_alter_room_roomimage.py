# Generated by Django 5.0.6 on 2024-06-08 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_alter_room_roomimage_alter_room_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='roomImage',
            field=models.ImageField(blank=True, null=True, upload_to='roomImages/'),
        ),
    ]
