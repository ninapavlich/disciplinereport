# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import carbon.atoms.models.media
import disciplinereport.s3utils


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secureimage',
            name='image',
            field=models.ImageField(help_text=b'To ensure a precise color replication in image variants, make sure an sRGB color profile has been assigned to each image.', storage=disciplinereport.s3utils._SecureMediaS3BotoStorage(bucket=b'disciplinereport-secure-dev', custom_domain=b'disciplinereport-secure-dev.s3.amazonaws.com', location=b'media'), null=True, upload_to=carbon.atoms.models.media.image_file_name, blank=True),
        ),
        migrations.AlterField(
            model_name='securemedia',
            name='file',
            field=models.FileField(storage=disciplinereport.s3utils._SecureMediaS3BotoStorage(bucket=b'disciplinereport-secure-dev', custom_domain=b'disciplinereport-secure-dev.s3.amazonaws.com', location=b'media'), null=True, upload_to=carbon.atoms.models.media.media_file_name, blank=True),
        ),
    ]
