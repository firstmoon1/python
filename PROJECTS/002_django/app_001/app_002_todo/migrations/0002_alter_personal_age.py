# Generated by Django 4.1 on 2022-09-01 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_002_todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='age',
            field=models.IntegerField(verbose_name='Age'),
        ),
    ]