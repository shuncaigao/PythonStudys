# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-03-29 13:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomTrackRecord',
            new_name='CustomerTrackRecord',
        ),
    ]
