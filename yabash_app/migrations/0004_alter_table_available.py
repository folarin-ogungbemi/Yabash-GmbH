# Generated by Django 3.2.16 on 2022-11-19 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yabash_app', '0003_auto_20221119_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='available',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=1),
        ),
    ]
