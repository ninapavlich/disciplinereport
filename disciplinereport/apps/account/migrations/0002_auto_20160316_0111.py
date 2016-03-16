# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('auth', '0006_require_contenttypes_0002'),
        ('media', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergroup',
            name='image',
            field=models.ForeignKey(related_name='account_usergroup_images', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='media.Image', help_text=b'Featured image', null=True),
        ),
        migrations.AddField(
            model_name='usergroup',
            name='modified_by',
            field=models.ForeignKey(related_name='account_usergroup_modified_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='usergroup',
            name='published_by',
            field=models.ForeignKey(related_name='account_usergroup_published_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='usergroup',
            name='social_share_image',
            field=models.ForeignKey(related_name='account_usergroup_social_images', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='media.Image', help_text=b'Standards for the social share image vary, but an image at least 300x200px should work well.', null=True),
        ),
        migrations.AddField(
            model_name='usergroup',
            name='template',
            field=models.ForeignKey(blank=True, to='core.Template', help_text=b'Template for view', null=True),
        ),
        migrations.AddField(
            model_name='socialcontactlink',
            name='created_by',
            field=models.ForeignKey(related_name='account_socialcontactlink_created_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='socialcontactlink',
            name='modified_by',
            field=models.ForeignKey(related_name='account_socialcontactlink_modified_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='socialcontactlink',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='organizationsocialcontactlink',
            name='created_by',
            field=models.ForeignKey(related_name='account_organizationsocialcontactlink_created_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='organizationsocialcontactlink',
            name='modified_by',
            field=models.ForeignKey(related_name='account_organizationsocialcontactlink_modified_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='organizationsocialcontactlink',
            name='organization',
            field=models.ForeignKey(to='account.Organization'),
        ),
        migrations.AddField(
            model_name='organizationsocialcontactlink',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='organizationmember',
            name='created_by',
            field=models.ForeignKey(related_name='account_organizationmember_created_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='organizationmember',
            name='modified_by',
            field=models.ForeignKey(related_name='account_organizationmember_modified_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='organizationmember',
            name='organization',
            field=models.ForeignKey(blank=True, to='account.Organization', null=True),
        ),
        migrations.AddField(
            model_name='organizationmember',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='created_by',
            field=models.ForeignKey(related_name='account_organization_created_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='creator',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='image',
            field=models.ForeignKey(related_name='account_organization_images', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='media.Image', help_text=b'Featured image', null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='modified_by',
            field=models.ForeignKey(related_name='account_organization_modified_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='published_by',
            field=models.ForeignKey(related_name='account_organization_published_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='social_share_image',
            field=models.ForeignKey(related_name='account_organization_social_images', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='media.Image', help_text=b'Standards for the social share image vary, but an image at least 300x200px should work well.', null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='template',
            field=models.ForeignKey(blank=True, to='core.Template', help_text=b'Template for view', null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='created_by',
            field=models.ForeignKey(related_name='account_address_created_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='modified_by',
            field=models.ForeignKey(related_name='account_address_modified_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='created_by',
            field=models.ForeignKey(related_name='account_user_created_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ForeignKey(related_name='account_user_images', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='media.Image', help_text=b'Featured image', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='modified_by',
            field=models.ForeignKey(related_name='account_user_modified_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
        ),
    ]
