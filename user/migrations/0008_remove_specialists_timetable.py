# Generated by Django 4.0.2 on 2022-03-17 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_specialists_timetable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialists',
            name='timetable',
        ),
    ]
