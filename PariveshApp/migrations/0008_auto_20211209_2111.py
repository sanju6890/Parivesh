# Generated by Django 3.2.9 on 2021-12-09 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PariveshApp', '0007_auto_20211209_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantation',
            name='plant_pic',
            field=models.ImageField(blank=True, null=True, upload_to='plant_pics'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]