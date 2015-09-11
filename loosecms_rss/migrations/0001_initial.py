# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import loosecms.fields


class Migration(migrations.Migration):

    dependencies = [
        ('loosecms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rss',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text='Give the name of the rss.', max_length=50, verbose_name='title')),
                ('slug', models.SlugField(help_text='Give the slug of the rss', unique=True, verbose_name='slug')),
                ('feed', models.CharField(help_text='Give the feed url', max_length=200, verbose_name='feed')),
                ('timeout', models.IntegerField(help_text='Give the timeout to reload rss. If the values is 0, each time will begin request to feed url to download rss content(adding delaying).', verbose_name='timeout')),
                ('image', loosecms.fields.UploadFilePathField(recursive=True, upload_to=b'rss', blank=True, path=b'rss', verbose_name='image')),
                ('order', models.IntegerField(verbose_name='order')),
                ('published', models.BooleanField(default=True, verbose_name='published')),
            ],
        ),
        migrations.CreateModel(
            name='RssManager',
            fields=[
                ('plugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='loosecms.Plugin')),
                ('title', models.CharField(help_text='Give the name of the rss manager.', max_length=200, verbose_name='title')),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('utime', models.DateTimeField(auto_now=True)),
            ],
            bases=('loosecms.plugin',),
        ),
        migrations.AddField(
            model_name='rss',
            name='manager',
            field=models.ForeignKey(verbose_name='manager', to='loosecms_rss.RssManager', help_text='Select the rss manager.'),
        ),
    ]
