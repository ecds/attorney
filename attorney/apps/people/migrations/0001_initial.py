# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0001_initial'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grantee',
            fields=[
                ('grantee_id', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255, blank=True)),
                ('alt_location', models.ForeignKey(related_name='alt_location', blank=True, to='geo.Place', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GrantorName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255, blank=True)),
                ('event', models.ForeignKey(to='events.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Identifier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='grantee',
            name='identifiers',
            field=models.ManyToManyField(to='people.Identifier', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='grantee',
            name='professional_location',
            field=models.ForeignKey(related_name='professional_location', blank=True, to='geo.Place', null=True),
        ),
        migrations.AddField(
            model_name='grantee',
            name='standard_location',
            field=models.ForeignKey(related_name='standard_location', blank=True, to='geo.Place', null=True),
        ),
    ]
