# Generated by Django 3.1.3 on 2020-12-18 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0014_remove_timetable_class_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='class_t',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Accounts.classroom'),
        ),
    ]
