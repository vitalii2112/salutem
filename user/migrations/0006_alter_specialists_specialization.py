# Generated by Django 4.0.2 on 2022-03-17 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_specialists_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialists',
            name='specialization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.specializations'),
        ),
    ]