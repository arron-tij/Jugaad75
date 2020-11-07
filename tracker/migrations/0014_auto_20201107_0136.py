# Generated by Django 3.1.3 on 2020-11-06 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracker', '0013_lecture_copy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='friday_slot1_latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='friday_slot1_longitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='friday_slot2_latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='friday_slot2_longitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='friday_slot3_latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='friday_slot3_longitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='monday_slot1_latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='monday_slot1_longitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='monday_slot2_latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='monday_slot2_longitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='monday_slot3_latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='monday_slot3_longitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='thrusday_slot1_latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='thrusday_slot1_longitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='thrusday_slot2_latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='thrusday_slot2_longitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='thrusday_slot3_latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='thrusday_slot3_longitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='tuesday_slot1_latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='tuesday_slot1_longitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='tuesday_slot2_latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='tuesday_slot2_longitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='tuesday_slot3_latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='tuesday_slot3_longitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='wednesday_slot1_latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='wednesday_slot1_longitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='wednesday_slot2_latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='wednesday_slot2_longitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='wednesday_slot3_latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='wednesday_slot3_longitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.CreateModel(
            name='sdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot1', models.IntegerField(default=0)),
                ('slot2', models.IntegerField(default=0)),
                ('slot3', models.IntegerField(default=0)),
                ('slat', models.FloatField(default=0.0)),
                ('slong', models.FloatField(default=0.0)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
