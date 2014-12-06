# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tetristats', '0002_auto_20141204_0346'),
    ]

    operations = [
        migrations.AddField(
            model_name='stat',
            name='time',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
