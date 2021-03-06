# Generated by Django 3.2.6 on 2021-11-19 07:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('agric', '0005_auto_20211118_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio_data',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='agric.location'),
        ),
        migrations.AlterField(
            model_name='bio_data',
            name='marital_status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='agric.marital_status'),
        ),
        migrations.AlterField(
            model_name='bio_data',
            name='sex',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='agric.sex'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bio_data',
            name='value_chain',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='agric.value_chain'),
        ),
        migrations.AlterField(
            model_name='historicalbio_data',
            name='location',
            field=models.ForeignKey(blank=True, db_constraint=False, default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='agric.location'),
        ),
        migrations.AlterField(
            model_name='historicalbio_data',
            name='marital_status',
            field=models.ForeignKey(blank=True, db_constraint=False, default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='agric.marital_status'),
        ),
        migrations.AlterField(
            model_name='historicalbio_data',
            name='value_chain',
            field=models.ForeignKey(blank=True, db_constraint=False, default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='agric.value_chain'),
        ),
    ]
