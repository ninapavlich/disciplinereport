# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0013_auto_20160731_1953'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='county',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='school',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='schooldistrict',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='schooltype',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='state',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='stateregion',
            options={'ordering': ['title']},
        ),
        migrations.AddField(
            model_name='schooldatum',
            name='oss_soc',
            field=models.FloatField(help_text=b'Out of School Suspension rates per 100 students.', null=True, verbose_name='Out-of-school Suspensions per 100 Students of Color', blank=True),
        ),
        migrations.AddField(
            model_name='schooldatum',
            name='oss_white',
            field=models.FloatField(help_text=b'Out of School Suspension rates per 100 students.', null=True, verbose_name='Out-of-school Suspensions per 100 White Students', blank=True),
        ),
        migrations.AddField(
            model_name='schooldistrictdatum',
            name='oss_soc',
            field=models.FloatField(help_text=b'Out of School Suspension rates per 100 students.', null=True, verbose_name='Out-of-school Suspensions per 100 Students of Color', blank=True),
        ),
        migrations.AddField(
            model_name='schooldistrictdatum',
            name='oss_white',
            field=models.FloatField(help_text=b'Out of School Suspension rates per 100 students.', null=True, verbose_name='Out-of-school Suspensions per 100 White Students', blank=True),
        ),
        migrations.AddField(
            model_name='statedatum',
            name='oss_soc',
            field=models.FloatField(help_text=b'Out of School Suspension rates per 100 students.', null=True, verbose_name='Out-of-school Suspensions per 100 Students of Color', blank=True),
        ),
        migrations.AddField(
            model_name='statedatum',
            name='oss_white',
            field=models.FloatField(help_text=b'Out of School Suspension rates per 100 students.', null=True, verbose_name='Out-of-school Suspensions per 100 White Students', blank=True),
        ),
    ]
