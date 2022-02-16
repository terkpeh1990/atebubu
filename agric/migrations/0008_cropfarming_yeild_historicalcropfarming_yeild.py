# Generated by Django 3.2.6 on 2021-11-19 07:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agric', '0007_auto_20211119_0720'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalCropFarming_Yeild',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('yield_date', models.DateField(blank=True, editable=False)),
                ('yields', models.PositiveIntegerField(default=0)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('bio', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='agric.bio_data')),
                ('crop_farming', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='agric.crop_farming')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical crop farming_ yeild',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='CropFarming_Yeild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yield_date', models.DateField(auto_now_add=True)),
                ('yields', models.PositiveIntegerField(default=0)),
                ('bio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agric.bio_data')),
                ('crop_farming', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agric.crop_farming')),
            ],
        ),
    ]
