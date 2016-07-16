# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20160716_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='schooldistrict',
            name='county',
            field=models.ForeignKey(default=16, to='data.County'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schooldistrict',
            name='state_obj',
            field=models.ForeignKey(default=1, to='data.State'),
            preserve_default=False,
        ),
    ]
