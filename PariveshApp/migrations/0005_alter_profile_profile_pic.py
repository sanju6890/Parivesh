# Generated by Django 3.2.7 on 2021-11-07 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PariveshApp', '0004_auto_20211105_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='default_profile_pic.jpg', upload_to='profile_pics'),
        ),
    ]
