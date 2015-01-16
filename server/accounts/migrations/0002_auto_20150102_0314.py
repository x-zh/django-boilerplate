# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(null=True, verbose_name='Birth date', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(default=b'', max_length=255, verbose_name='Phone number'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(default=b'', max_length=255, verbose_name='Gender', choices=[(b'', b'Gender'), (b'M', b'Male'), (b'F', b'Female'), (b'P', b'Private')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(default=b'', max_length=255, verbose_name='Where you live'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(default=b'', max_length=255, verbose_name='Name'),
            preserve_default=True,
        ),
    ]
