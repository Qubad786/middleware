# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-09 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharing', '0004_afp_share_afp_timemachine_quota'),
    ]

    operations = [
        migrations.AddField(
            model_name='cifs_share',
            name='cifs_abe',
            field=models.BooleanField(default=False, verbose_name='Access Based Share Enumeration'),
        ),
    ]