# Generated by Django 3.2.4 on 2021-06-29 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduleapp', '0002_alter_schedule_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='event_date',
            field=models.DateTimeField(),
        ),
    ]
