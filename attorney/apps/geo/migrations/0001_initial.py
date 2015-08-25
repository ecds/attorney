# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('place_id', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('alt_name', models.CharField(max_length=255, blank=True)),
                ('lat', models.DecimalField(null=True, max_digits=9, decimal_places=6, blank=True)),
                ('lon', models.DecimalField(null=True, max_digits=9, decimal_places=6, blank=True)),
                ('uri', models.URLField(verbose_name=b'Geonames URL', blank=True)),
            ],
        ),
    ]
