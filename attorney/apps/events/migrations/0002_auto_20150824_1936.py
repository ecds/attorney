# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0001_initial'),
        ('events', '0001_initial'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='grantees',
            field=models.ManyToManyField(to='people.Grantee', blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(to='geo.Place', blank=True),
        ),
    ]
