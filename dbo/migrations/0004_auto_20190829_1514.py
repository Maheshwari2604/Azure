# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-08-29 15:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbo', '0003_auto_20190829_1510'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tasks',
            new_name='task',
        ),
    ]
