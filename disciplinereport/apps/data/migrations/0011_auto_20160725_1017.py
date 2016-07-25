# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0010_auto_20160724_2348'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schooldatum',
            old_name='district_inequality_contribution',
            new_name='inequality_contribution',
        ),
        migrations.RenameField(
            model_name='schooldistrictdatum',
            old_name='district_inequality_contribution',
            new_name='inequality_contribution',
        ),
        migrations.RenameField(
            model_name='statedatum',
            old_name='district_inequality_contribution',
            new_name='inequality_contribution',
        ),
    ]
