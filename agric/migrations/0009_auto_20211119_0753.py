# Generated by Django 3.2.6 on 2021-11-19 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agric', '0008_cropfarming_yeild_historicalcropfarming_yeild'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cropfarming_yeild',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='historicalcropfarming_yeild',
            name='bio',
        ),
    ]
