# Generated by Django 3.2.16 on 2022-11-26 20:27

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yabash_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Headline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headtext', models.CharField(max_length=300)),
                ('subtext', models.CharField(max_length=300)),
                ('headline_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('headline_info', models.CharField(max_length=100)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
            ],
        ),
    ]
