# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('citation', models.CharField(max_length=20)),
                ('date', models.IntegerField()),
                ('power_type', models.CharField(max_length=10, verbose_name=b'Type of Power')),
                ('cabildo', models.CharField(max_length=50)),
                ('translator', models.CharField(max_length=50, blank=True)),
                ('translation_detail', models.CharField(max_length=100, blank=True)),
                ('description', models.CharField(max_length=255, blank=True)),
            ],
        ),
    ]
