# Generated by Django 2.1.3 on 2018-11-19 20:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sauna_occupancies', '0002_auto_20181119_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occupancy',
            name='start',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
