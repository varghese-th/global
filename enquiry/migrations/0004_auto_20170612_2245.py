# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 17:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0003_auto_20170611_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enquiry',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='enquiry',
            name='email',
        ),
        migrations.RemoveField(
            model_name='enquiry',
            name='enquiry',
        ),
        migrations.RemoveField(
            model_name='enquiry',
            name='sname',
        ),
    ]
