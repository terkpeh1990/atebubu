# Generated by Django 3.2.6 on 2021-11-19 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agric', '0006_auto_20211119_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio_data',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agric.location'),
        ),
        migrations.AlterField(
            model_name='bio_data',
            name='marital_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agric.marital_status'),
        ),
        migrations.AlterField(
            model_name='bio_data',
            name='value_chain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agric.value_chain'),
        ),
        migrations.AlterField(
            model_name='historicalbio_data',
            name='location',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='agric.location'),
        ),
        migrations.AlterField(
            model_name='historicalbio_data',
            name='marital_status',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='agric.marital_status'),
        ),
        migrations.AlterField(
            model_name='historicalbio_data',
            name='value_chain',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='agric.value_chain'),
        ),
    ]
