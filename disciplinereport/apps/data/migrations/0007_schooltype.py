# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0002_auto_20160326_0447'),
        ('page', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_menuitem_url'),
        ('data', '0006_statedatum'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date', null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date', null=True)),
                ('admin_note', models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True)),
                ('title', models.CharField(help_text=b'The display title for this object.', max_length=255, null=True, verbose_name='Title', blank=True)),
                ('slug', models.CharField(help_text=b'Auto-generated page slug for this object.', max_length=255, verbose_name='Slug', db_index=True, blank=True)),
                ('uuid', models.CharField(help_text=b'UUID generated for object; can be used for short URLs', max_length=255, verbose_name='UUID', blank=True)),
                ('order', models.IntegerField(default=0, help_text=b'')),
                ('path', models.CharField(help_text=b'Actual path used based on generated and override path', max_length=255, null=True, verbose_name='path', blank=True)),
                ('title_path', models.CharField(help_text=b'Actual path used based on generated and override path', max_length=255, null=True, verbose_name='title path', blank=True)),
                ('path_generated', models.CharField(help_text=b'The URL path to this page, based on page hierarchy and slug.', max_length=255, null=True, verbose_name='generated path', blank=True)),
                ('path_override', models.CharField(help_text=b'The URL path to this page, defined absolutely.', max_length=255, null=True, verbose_name='path override', blank=True)),
                ('hierarchy', models.CharField(null=True, max_length=255, blank=True, help_text=b'Administrative Hierarchy', unique=True, verbose_name='hierarchy')),
                ('temporary_redirect', models.CharField(help_text=b'Temporarily redirect to a different path', max_length=255, verbose_name='Temporary Redirect', blank=True)),
                ('permanent_redirect', models.CharField(help_text=b'Permanently redirect to a different path', max_length=255, verbose_name='Permanent Redirect', blank=True)),
                ('publication_date', models.DateTimeField(null=True, verbose_name='Publication Date', blank=True)),
                ('publication_status', models.IntegerField(default=10, help_text=b'Current publication status', choices=[(10, 'Draft'), (20, 'Needs Review'), (100, 'Published'), (40, 'Unpublished')])),
                ('publish_on_date', models.DateTimeField(help_text=b"Object state will be set to 'Published' on this date.", null=True, verbose_name='Publish on Date', blank=True)),
                ('expire_on_date', models.DateTimeField(help_text=b"Object state will be set to 'Expired' on this date.", null=True, verbose_name='Expire on Date', blank=True)),
                ('page_meta_description', models.CharField(help_text=b'A short description of the page, used for SEO and not displayed to the user; aim for 150-160 characters.', max_length=2000, verbose_name='Meta Description', blank=True)),
                ('page_meta_keywords', models.CharField(help_text=b'A short list of keywords of the page, used for SEO and not displayed to the user; aim for 150-160 characters.', max_length=2000, verbose_name='Meta Page Keywords', blank=True)),
                ('is_searchable', models.BooleanField(default=True, help_text=b'Allow search engines to index this object and display in sitemap.')),
                ('in_sitemap', models.BooleanField(default=True, help_text=b'Is in sitemap')),
                ('noindex', models.BooleanField(default=False, help_text=b'Robots noindex')),
                ('nofollow', models.BooleanField(default=False, help_text=b'Robots nofollow')),
                ('sitemap_changefreq', models.CharField(default=b'monthly', help_text=b'How frequently does page content update', max_length=255, verbose_name='Sitemap Change Frequency', choices=[(b'never', 'Never'), (b'yearly', 'Yearly'), (b'monthly', 'Monthly'), (b'weekly', 'Weekly'), (b'daily', 'Daily'), (b'hourly', 'Hourly'), (b'always', 'Always')])),
                ('sitemap_priority', models.CharField(default=b'0.5', max_length=255, blank=True, help_text=b'Sitemap priority', null=True, verbose_name=b'Sitemap Priority')),
                ('shareable', models.BooleanField(default=False, help_text=b'Show sharing widget')),
                ('tiny_url', models.CharField(help_text=b'Tiny URL used for social sharing', max_length=255, null=True, verbose_name='tiny url', blank=True)),
                ('social_share_type', models.CharField(default=b'article', choices=[(b'article', b'Article'), (b'book', b'Book'), (b'profile', b'Profile'), (b'website', b'Website'), (b'video.movie', b'Video - Movie'), (b'video.episode', b'Video - Episode'), (b'video.tv_show', b'Video - TV Show'), (b'video.other', b'Video - Other'), (b'music.song', b'Music - Song'), (b'music.album', b'Music - Album'), (b'music.radio_station', b'Music - Playlist'), (b'music.radio_station', b'Music - Radio Station')], max_length=255, blank=True, null=True, verbose_name=b'Social type')),
                ('facebook_author_id', models.CharField(help_text=b'Numeric Facebook ID', max_length=255, null=True, verbose_name=b'Facebook Author ID', blank=True)),
                ('twitter_author_id', models.CharField(help_text=b'Twitter handle, including "@" e.g. @cgpartners', max_length=255, null=True, verbose_name=b'Twitter Admin ID', blank=True)),
                ('google_author_id', models.CharField(help_text=b'Google author id, e.g. the AUTHOR_ID in https://plus.google.com/AUTHOR_ID/posts', max_length=255, null=True, verbose_name=b'Google Admin ID', blank=True)),
                ('content', models.TextField(help_text=b'', null=True, verbose_name='content', blank=True)),
                ('synopsis', models.TextField(help_text=b'', null=True, verbose_name='synopsis', blank=True)),
                ('street_1', models.CharField(max_length=30, null=True, verbose_name='Street Address 1', blank=True)),
                ('street_2', models.CharField(max_length=30, null=True, verbose_name='Street Address 2', blank=True)),
                ('city', models.CharField(max_length=30, null=True, verbose_name='City', blank=True)),
                ('state', models.CharField(max_length=30, null=True, verbose_name='State', blank=True)),
                ('zipcode', models.CharField(max_length=30, null=True, verbose_name='Zipcode', blank=True)),
                ('latitude', models.CharField(max_length=30, null=True, verbose_name='Latitude', blank=True)),
                ('longitude', models.CharField(max_length=30, null=True, verbose_name='Longitude', blank=True)),
                ('email', models.CharField(max_length=255, null=True, verbose_name='Email', blank=True)),
                ('phone_number', models.CharField(max_length=255, null=True, verbose_name='Phone Number', blank=True)),
                ('website', models.CharField(max_length=255, null=True, verbose_name='Website', blank=True)),
                ('created_by', models.ForeignKey(related_name='data_schooltype_created_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('image', models.ForeignKey(related_name='data_schooltype_images', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='media.Image', help_text=b'Featured image', null=True)),
                ('modified_by', models.ForeignKey(related_name='data_schooltype_modified_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='page.Page', null=True)),
                ('published_by', models.ForeignKey(related_name='data_schooltype_published_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('social_share_image', models.ForeignKey(related_name='data_schooltype_social_images', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='media.Image', help_text=b'Standards for the social share image vary, but an image at least 300x200px should work well.', null=True)),
                ('template', models.ForeignKey(blank=True, to='core.Template', help_text=b'Template for view', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
