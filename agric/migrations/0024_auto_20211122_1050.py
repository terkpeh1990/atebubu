# Generated by Django 3.2.6 on 2021-11-22 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agric', '0023_alter_business_info_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalland',
            name='bio',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='agric.bio_data'),
        ),
        migrations.AddField(
            model_name='land',
            name='bio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='agric.bio_data'),
        ),
    ]
