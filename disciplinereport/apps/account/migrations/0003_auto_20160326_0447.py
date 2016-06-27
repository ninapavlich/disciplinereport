# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20160316_0111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organizationsocialcontactlink',
            options={'ordering': ['order']},
        ),
        migrations.RemoveField(
            model_name='user',
            name='directory_contact_description',
        ),
        migrations.RemoveField(
            model_name='user',
            name='job_title',
        ),
        migrations.AddField(
            model_name='user',
            name='project_role',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
