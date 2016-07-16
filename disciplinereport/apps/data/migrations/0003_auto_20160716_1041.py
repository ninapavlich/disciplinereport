# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20160709_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='schooldistrict',
            name='state_region',
            field=models.ForeignKey(default=1, to='data.StateRegion'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='school',
            name='email',
            field=models.CharField(max_length=255, null=True, verbose_name='Email', blank=True),
        ),
        migrations.AlterField(
            model_name='schooldistrict',
            name='email',
            field=models.CharField(max_length=255, null=True, verbose_name='Email', blank=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='email',
            field=models.CharField(max_length=255, null=True, verbose_name='Email', blank=True),
        ),
        migrations.AlterField(
            model_name='stateregion',
            name='email',
            field=models.CharField(max_length=255, null=True, verbose_name='Email', blank=True),
        ),
    ]
