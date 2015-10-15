# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_grantee_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grantee',
            old_name='standard_location',
            new_name='location',
        ),
        migrations.RemoveField(
            model_name='grantee',
            name='professional_location',
        ),
    ]
