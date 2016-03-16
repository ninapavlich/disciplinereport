# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date', null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date', null=True)),
                ('admin_note', models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True)),
                ('title', models.CharField(help_text=b'The display title for this object.', max_length=255, null=True, verbose_name='Title', blank=True)),
                ('slug', models.CharField(help_text=b'Auto-generated page slug for this object.', max_length=255, verbose_name='Slug', db_index=True, blank=True)),
                ('can_be_viewed_online', models.BooleanField(default=False, help_text=b'Allow recipients to view this online. DO NOT ENABLE if you are sending any kind of private data in this email category.')),
                ('requires_explicit_opt_in', models.BooleanField(default=False, help_text=b'Sending these emails require user to explicitely opt-in to category.')),
                ('can_unsubscribe', models.BooleanField(default=True, help_text=b'If these emails are transactional, then subscribe/unsubscribe functionality is not needed')),
                ('created_by', models.ForeignKey(related_name='email_emailcategory_created_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='email_emailcategory_modified_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='email.EmailCategory', null=True)),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'Email categories',
            },
        ),
        migrations.CreateModel(
            name='EmailCategorySubscriptionSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date', null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date', null=True)),
                ('admin_note', models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True)),
                ('title', models.CharField(help_text=b'The display title for this object.', max_length=255, null=True, verbose_name='Title', blank=True)),
                ('slug', models.CharField(help_text=b'Auto-generated page slug for this object.', max_length=255, verbose_name='Slug', db_index=True, blank=True)),
                ('status', models.CharField(default=b'default', max_length=255, choices=[(b'default', 'Default'), (b'unsubscribed', 'Unsubscribed'), (b'subscribed', 'Subscribed')])),
                ('category', models.ForeignKey(to='email.EmailCategory')),
                ('created_by', models.ForeignKey(related_name='email_emailcategorysubscriptionsettings_created_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='email_emailcategorysubscriptionsettings_modified_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'Email Category subscription settings',
            },
        ),
        migrations.CreateModel(
            name='EmailReceipt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date', null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date', null=True)),
                ('admin_note', models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True)),
                ('access_key', models.CharField(max_length=50, unique=True, null=True, verbose_name='key', blank=True)),
                ('recipient_email', models.CharField(max_length=255, verbose_name='Recipient Email')),
                ('rendered_subject', models.TextField(null=True, verbose_name='Rendered Subject', blank=True)),
                ('rendered_body', models.TextField(null=True, verbose_name='Rendered Body', blank=True)),
                ('viewed', models.BooleanField(default=False)),
                ('viewed_from_email', models.BooleanField(default=False)),
                ('viewed_online', models.BooleanField(default=False)),
                ('view_count', models.PositiveIntegerField(default=0, null=True, verbose_name=b'View Count', blank=True)),
                ('first_viewed_date', models.DateTimeField(null=True, verbose_name='First Viewed Date', blank=True)),
                ('last_viewed_date', models.DateTimeField(null=True, verbose_name='Last Viewed Date', blank=True)),
                ('sending_error', models.BooleanField(default=False)),
                ('sending_error_message', models.TextField(null=True, blank=True)),
                ('category', models.ForeignKey(to='email.EmailCategory')),
                ('created_by', models.ForeignKey(related_name='email_emailreceipt_created_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='email_emailreceipt_modified_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date', null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date', null=True)),
                ('admin_note', models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True)),
                ('title', models.CharField(help_text=b'The display title for this object.', max_length=255, null=True, verbose_name='Title', blank=True)),
                ('slug', models.CharField(help_text=b'Auto-generated page slug for this object.', max_length=255, verbose_name='Slug', db_index=True, blank=True)),
                ('body_template', models.TextField(help_text=b'Template used for email body', null=True, verbose_name='body template', blank=True)),
                ('subject_template', models.TextField(help_text=b'Template used for email subject', null=True, verbose_name='subject template', blank=True)),
                ('created_by', models.ForeignKey(related_name='email_emailtemplate_created_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='email_emailtemplate_modified_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserSubscriptionSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date', null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date', null=True)),
                ('admin_note', models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True)),
                ('access_key', models.CharField(max_length=50, unique=True, null=True, verbose_name='key', blank=True)),
                ('recipient_email', models.CharField(max_length=255, verbose_name='Recipient Email')),
                ('created_by', models.ForeignKey(related_name='email_usersubscriptionsettings_created_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='email_usersubscriptionsettings_modified_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'User subscription settings',
            },
        ),
        migrations.AddField(
            model_name='emailcategorysubscriptionsettings',
            name='parent',
            field=models.ForeignKey(to='email.UserSubscriptionSettings'),
        ),
    ]
