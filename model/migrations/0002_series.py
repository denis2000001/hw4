# Generated by Django 4.1.1 on 2022-09-24 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series_name', models.CharField(max_length=50)),
                ('model_photo', models.ImageField(blank=True, null=True, upload_to='model_photo')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.model')),
            ],
        ),
    ]