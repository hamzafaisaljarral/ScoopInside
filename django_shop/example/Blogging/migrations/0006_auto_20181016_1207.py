# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-16 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogging', '0005_auto_20181016_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='images',
            field=models.FileField(blank=True, upload_to='blog_image'),
        ),
    ]
