# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 10:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0007_auto_20170619_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='address',
            field=models.TextField(default=''),
        ),
    ]
