# Generated by Django 3.0.6 on 2020-06-08 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Formvalidation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(blank=True),
        ),
    ]
