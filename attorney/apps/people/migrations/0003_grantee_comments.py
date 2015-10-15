# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20150824_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='grantee',
            name='comments',
            field=models.TextField(blank=True),
        ),
    ]
