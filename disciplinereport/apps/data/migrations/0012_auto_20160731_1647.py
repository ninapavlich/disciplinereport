# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0011_auto_20160725_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schooldatum',
            name='inequality_contribution',
            field=models.FloatField(help_text=b'', null=True, verbose_name='Inequality Contribution', blank=True),
        ),
        migrations.AlterField(
            model_name='schooldistrictdatum',
            name='inequality_contribution',
            field=models.FloatField(help_text=b'', null=True, verbose_name='Inequality Contribution', blank=True),
        ),
        migrations.AlterField(
            model_name='statedatum',
            name='inequality_contribution',
            field=models.FloatField(help_text=b'', null=True, verbose_name='Inequality Contribution', blank=True),
        ),
    ]
