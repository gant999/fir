# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-01-04 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fir_abuse', '0006_auto_20170103_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abusecontact',
            name='bcc',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='abusecontact',
            name='cc',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
    ]