# Generated by Django 4.1.1 on 2022-09-26 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0002_series'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='series',
            name='model_photo',
        ),
        migrations.AddField(
            model_name='model',
            name='model_photo',
            field=models.ImageField(blank=True, null=True, upload_to='model_photo'),
        ),
        migrations.AddField(
            model_name='series',
            name='series_photo',
            field=models.ImageField(blank=True, null=True, upload_to='series_photo'),
        ),
    ]
