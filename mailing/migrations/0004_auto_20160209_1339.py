# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-09 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0003_auto_20160205_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='template_file',
            field=models.FileField(blank=True, help_text='Leave blank to use mailing/{key}.html from within your template directories.', upload_to='mailing/templates', verbose_name='template file'),
        ),
    ]
