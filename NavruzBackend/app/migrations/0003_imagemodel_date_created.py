# Generated by Django 4.0 on 2025-03-18 08:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_trashbin_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
