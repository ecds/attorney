# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20150824_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.ForeignKey(blank=True, to='geo.Place', null=True),
        ),
    ]
