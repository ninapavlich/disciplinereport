# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='url',
            field=models.CharField(max_length=255, null=True, verbose_name='URL', blank=True),
        ),
    ]
