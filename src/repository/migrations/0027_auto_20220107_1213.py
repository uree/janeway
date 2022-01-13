# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-01-07 12:13
from __future__ import unicode_literals

import core.file_system
import core.model_utils
from django.db import migrations, models
from django.conf import settings
import repository.models


def remove_stale_domains(apps, schema_editor):
    if hasattr(settings, 'URL_CONFIG') and settings.URL_CONFIG == 'path':
        Repository = apps.get_model('repository', 'Repository')
        Repository.objects.all().update(domain=None)


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0026_merge_20211011_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='domain',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.RunPython(
            remove_stale_domains, reverse_code=migrations.RunPython.noop
        ),
        migrations.AlterField(
            model_name='preprint',
            name='keywords',
            field=core.model_utils.M2MOrderedThroughField(blank=True, null=True, through='repository.KeywordPreprint', to='submission.Keyword'),
        ),
        migrations.AlterField(
            model_name='repository',
            name='hero_background',
            field=core.model_utils.SVGImageField(blank=True, null=True, storage=core.file_system.JanewayFileSystemStorage(), upload_to=repository.models.repo_media_upload),
        ),
        migrations.AlterField(
            model_name='repository',
            name='logo',
            field=core.model_utils.SVGImageField(blank=True, null=True, storage=core.file_system.JanewayFileSystemStorage(), upload_to=repository.models.repo_media_upload),
        ),
        migrations.AlterField(
            model_name='versionqueue',
            name='title',
            field=models.CharField(help_text='Your article title', max_length=300),
        ),
    ]