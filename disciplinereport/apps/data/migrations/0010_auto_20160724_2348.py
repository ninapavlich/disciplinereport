# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_tooltip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schooldatum',
            name='expulsions',
            field=models.FloatField(help_text=b'Expulsions per 100 students.', null=True, verbose_name='Expulsions', blank=True),
        ),
        migrations.AlterField(
            model_name='schooldatum',
            name='school_arrests',
            field=models.FloatField(help_text=b'School related arrests per 100 students.', null=True, verbose_name='School Arrests', blank=True),
        ),
        migrations.AlterField(
            model_name='schooldistrictdatum',
            name='expulsions',
            field=models.FloatField(help_text=b'Expulsions per 100 students.', null=True, verbose_name='Expulsions', blank=True),
        ),
        migrations.AlterField(
            model_name='schooldistrictdatum',
            name='school_arrests',
            field=models.FloatField(help_text=b'School related arrests per 100 students.', null=True, verbose_name='School Arrests', blank=True),
        ),
        migrations.AlterField(
            model_name='statedatum',
            name='expulsions',
            field=models.FloatField(help_text=b'Expulsions per 100 students.', null=True, verbose_name='Expulsions', blank=True),
        ),
        migrations.AlterField(
            model_name='statedatum',
            name='school_arrests',
            field=models.FloatField(help_text=b'School related arrests per 100 students.', null=True, verbose_name='School Arrests', blank=True),
        ),
    ]
