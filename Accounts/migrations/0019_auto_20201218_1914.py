# Generated by Django 3.1.3 on 2020-12-18 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0018_timetable_class_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='class_time',
            field=models.TimeField(),
        ),
    ]
