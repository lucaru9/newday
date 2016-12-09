# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-11-25 22:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0002_auto_20161125_1549'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='couponuser',
            options={'ordering': ['-created_at'], 'verbose_name': 'Cupon Usuario', 'verbose_name_plural': 'Cupones Usuario'},
        ),
        migrations.AddField(
            model_name='couponuser',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 11, 25, 22, 15, 53, 221607, tzinfo=utc)),
            preserve_default=False,
        ),
    ]