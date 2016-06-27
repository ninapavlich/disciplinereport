# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20160326_0447'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationsocialcontactlink',
            name='css_classes',
            field=models.CharField(default=b'', max_length=255, blank=True, help_text=b'Extra css classes to add to the item', null=True, verbose_name='CSS Classes'),
        ),
        migrations.AddField(
            model_name='organizationsocialcontactlink',
            name='extra_attributes',
            field=models.CharField(default=b'', max_length=255, blank=True, help_text=b'Extra attributes to add to the item', null=True, verbose_name='Extra Attributes'),
        ),
        migrations.AddField(
            model_name='organizationsocialcontactlink',
            name='target',
            field=models.CharField(default=b'_self', help_text=b'', max_length=255, verbose_name='Target', choices=[(b'_blank', '_blank'), (b'_self', '_self'), (b'_parent', '_parent'), (b'_top', '_top')]),
        ),
        migrations.AddField(
            model_name='socialcontactlink',
            name='css_classes',
            field=models.CharField(default=b'', max_length=255, blank=True, help_text=b'Extra css classes to add to the item', null=True, verbose_name='CSS Classes'),
        ),
        migrations.AddField(
            model_name='socialcontactlink',
            name='extra_attributes',
            field=models.CharField(default=b'', max_length=255, blank=True, help_text=b'Extra attributes to add to the item', null=True, verbose_name='Extra Attributes'),
        ),
        migrations.AddField(
            model_name='socialcontactlink',
            name='target',
            field=models.CharField(default=b'_self', help_text=b'', max_length=255, verbose_name='Target', choices=[(b'_blank', '_blank'), (b'_self', '_self'), (b'_parent', '_parent'), (b'_top', '_top')]),
        ),
    ]
