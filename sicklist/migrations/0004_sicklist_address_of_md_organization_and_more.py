# Generated by Django 4.0.2 on 2022-04-10 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sicklist', '0003_alter_sicklist_disability_code_addit'),
    ]

    operations = [
        migrations.AddField(
            model_name='sicklist',
            name='address_of_md_organization',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='sicklist',
            name='md_organization',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]