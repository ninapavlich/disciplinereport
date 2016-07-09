# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schooldatum',
            name='ratial_disparity_impact',
        ),
        migrations.RemoveField(
            model_name='schooldistrictdatum',
            name='ratial_disparity_impact',
        ),
        migrations.AddField(
            model_name='school',
            name='email',
            field=models.CharField(max_length=255, null=True, verbose_name='Home Phone', blank=True),
        ),
        migrations.AddField(
            model_name='school',
            name='phone_number',
            field=models.CharField(max_length=255, null=True, verbose_name='Phone Number', blank=True),
        ),
        migrations.AddField(
            model_name='school',
            name='website',
            field=models.CharField(max_length=255, null=True, verbose_name='Website', blank=True),
        ),
        migrations.AddField(
            model_name='schooldatum',
            name='expulsions',
            field=models.FloatField(help_text=b'', null=True, verbose_name='Expulsions', blank=True),
        ),
        migrations.AddField(
            model_name='schooldatum',
            name='racial_disparity_impact',
            field=models.FloatField(help_text=b'', null=True, verbose_name='Racial Disparity Impact', blank=True),
        ),
        migrations.AddField(
            model_name='schooldatum',
            name='school_arrests',
            field=models.FloatField(help_text=b'', null=True, verbose_name='School Arrests', blank=True),
        ),
        migrations.AddField(
            model_name='schooldistrict',
            name='email',
            field=models.CharField(max_length=255, null=True, verbose_name='Home Phone', blank=True),
        ),
        migrations.AddField(
            model_name='schooldistrict',
            name='phone_number',
            field=models.CharField(max_length=255, null=True, verbose_name='Phone Number', blank=True),
        ),
        migrations.AddField(
            model_name='schooldistrict',
            name='website',
            field=models.CharField(max_length=255, null=True, verbose_name='Website', blank=True),
        ),
        migrations.AddField(
            model_name='schooldistrictdatum',
            name='district_inequality_contribution',
            field=models.FloatField(help_text=b'', null=True, verbose_name='District Inequality Contribution', blank=True),
        ),
        migrations.AddField(
            model_name='schooldistrictdatum',
            name='expulsions',
            field=models.FloatField(help_text=b'', null=True, verbose_name='Expulsions', blank=True),
        ),
        migrations.AddField(
            model_name='schooldistrictdatum',
            name='racial_disparity_impact',
            field=models.FloatField(help_text=b'', null=True, verbose_name='Racial Disparity Impact', blank=True),
        ),
        migrations.AddField(
            model_name='schooldistrictdatum',
            name='school_arrests',
            field=models.FloatField(help_text=b'', null=True, verbose_name='School Arrests', blank=True),
        ),
        migrations.AddField(
            model_name='state',
            name='email',
            field=models.CharField(max_length=255, null=True, verbose_name='Home Phone', blank=True),
        ),
        migrations.AddField(
            model_name='state',
            name='phone_number',
            field=models.CharField(max_length=255, null=True, verbose_name='Phone Number', blank=True),
        ),
        migrations.AddField(
            model_name='state',
            name='website',
            field=models.CharField(max_length=255, null=True, verbose_name='Website', blank=True),
        ),
        migrations.AddField(
            model_name='stateregion',
            name='email',
            field=models.CharField(max_length=255, null=True, verbose_name='Home Phone', blank=True),
        ),
        migrations.AddField(
            model_name='stateregion',
            name='phone_number',
            field=models.CharField(max_length=255, null=True, verbose_name='Phone Number', blank=True),
        ),
        migrations.AddField(
            model_name='stateregion',
            name='website',
            field=models.CharField(max_length=255, null=True, verbose_name='Website', blank=True),
        ),
    ]
