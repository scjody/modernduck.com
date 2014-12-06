# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tetristats', '0003_stat_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='stat',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0), auto_now=True),
            preserve_default=False,
        ),
    ]
