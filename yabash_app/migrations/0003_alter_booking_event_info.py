# Generated by Django 3.2.16 on 2022-11-27 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yabash_app', '0002_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='event_info',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]