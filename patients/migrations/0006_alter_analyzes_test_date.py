# Generated by Django 4.0.2 on 2022-02-23 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_remove_analyzes_patient_analyzes_patient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analyzes',
            name='test_date',
            field=models.DateTimeField(blank=True),
        ),
    ]