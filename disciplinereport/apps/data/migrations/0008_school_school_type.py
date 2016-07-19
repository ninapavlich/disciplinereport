# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_schooltype'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='school_type',
            field=models.ForeignKey(default=1, to='data.SchoolType'),
            preserve_default=False,
        ),
    ]
