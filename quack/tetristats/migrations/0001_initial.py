# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.CharField(max_length=36)),
                ('total_gas', models.FloatField()),
                ('score', models.IntegerField()),
                ('lines', models.IntegerField()),
                ('complete', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
