# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-11-25 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='code',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='C\xf3digo'),
        ),
    ]
