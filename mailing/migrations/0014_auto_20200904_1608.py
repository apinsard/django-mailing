# Generated by Django 3.0.9 on 2020-09-04 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0013_auto_20200330_1220'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='campaign',
            options={'ordering': ['key'], 'verbose_name': 'e-mail campaign', 'verbose_name_plural': 'e-mail campaigns'},
        ),
    ]
