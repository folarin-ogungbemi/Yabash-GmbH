# Generated by Django 3.2.16 on 2022-11-20 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yabash_app', '0011_rename_no_of_guest_booking_number_of_guest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='number_of_guest',
            field=models.ForeignKey(default='2 People', on_delete=django.db.models.deletion.CASCADE, related_name='table_capacity', to='yabash_app.table'),
        ),
    ]
