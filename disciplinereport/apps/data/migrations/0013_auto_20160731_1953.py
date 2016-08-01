# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0012_auto_20160731_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schooldistrict',
            name='county',
            field=models.ForeignKey(blank=True, to='data.County', null=True),
        ),
        migrations.AlterField(
            model_name='schooldistrict',
            name='state_obj',
            field=models.ForeignKey(blank=True, to='data.State', null=True),
        ),
        migrations.AlterField(
            model_name='schooldistrict',
            name='state_region',
            field=models.ForeignKey(blank=True, to='data.StateRegion', null=True),
        ),
    ]
