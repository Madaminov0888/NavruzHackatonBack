# Generated by Django 4.0 on 2025-03-18 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trashbin',
            name='images',
            field=models.ManyToManyField(blank=True, default=None, to='app.ImageModel'),
        ),
    ]
