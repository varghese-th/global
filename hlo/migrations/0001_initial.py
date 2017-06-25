# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.TextField(default='')),
                ('contact', models.CharField(default='', max_length=25)),
                ('email', models.CharField(default='', max_length=25)),
                ('enquiry', models.TextField(default='')),
            ],
        ),
    ]
