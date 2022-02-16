# Generated by Django 3.2.6 on 2021-11-19 13:30

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('agric', '0014_auto_20211119_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='bio_association',
            name='role',
            field=models.CharField(choices=[('Executive', 'Executive'), ('Member', 'Member')], default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalbio_association',
            name='role',
            field=models.CharField(choices=[('Executive', 'Executive'), ('Member', 'Member')], default=datetime.datetime(2021, 11, 19, 13, 30, 3, 937023, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
    ]
