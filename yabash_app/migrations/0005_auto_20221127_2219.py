# Generated by Django 3.2.16 on 2022-11-27 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yabash_app', '0004_auto_20221127_2143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='booked_table',
        ),
        migrations.RemoveField(
            model_name='table',
            name='hour_ID',
        ),
        migrations.RemoveField(
            model_name='table',
            name='table_status',
        ),
        migrations.RemoveField(
            model_name='table',
            name='updated_on',
        ),
        migrations.AlterField(
            model_name='booking',
            name='event_time',
            field=models.CharField(choices=[('08:00 am', '08:00 am'), ('09:00 am', '09:00 am'), ('10:00 am', '10:00 am'), ('11:00 am', '11:00 am'), ('12:00 pm', '12:00 pm'), ('13:00 pm', '13:00 pm'), ('14:00 pm', '14:00 pm'), ('15:00 pm', '15:00 pm'), ('16:00 pm', '16:00 pm'), ('17:00 pm', '17:00 pm'), ('18:00 pm', '18:00 pm'), ('19:00 pm', '19:00 pm'), ('20:00 pm', '20:00 pm'), ('21:00 pm', '21:00 pm'), ('22:00 pm', '22:00 pm')], default='08:00 am', max_length=10),
        ),
        migrations.AlterField(
            model_name='booking',
            name='number_of_guest',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='table_capacity', to='yabash_app.table'),
        ),
        migrations.DeleteModel(
            name='Hour',
        ),
    ]