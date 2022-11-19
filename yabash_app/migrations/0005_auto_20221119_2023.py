# Generated by Django 3.2.16 on 2022-11-19 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yabash_app', '0004_alter_table_available'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='table',
            options={'ordering': ['-created_on']},
        ),
        migrations.AddField(
            model_name='table',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='available',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=0),
        ),
    ]
