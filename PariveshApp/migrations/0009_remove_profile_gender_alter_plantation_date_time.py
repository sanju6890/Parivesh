# Generated by Django 4.0.3 on 2022-04-08 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PariveshApp', '0008_auto_20211209_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='gender',
        ),
        migrations.AlterField(
            model_name='plantation',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
