# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-05-31 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField(blank=True)),
                ('from_email', models.TextField(blank=True)),
                ('recipient_list', models.TextField(blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Created in')),
                ('failed', models.NullBooleanField(default=None)),
            ],
        ),
    ]