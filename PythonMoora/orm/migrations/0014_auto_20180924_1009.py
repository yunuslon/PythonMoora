# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-24 10:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0013_auto_20180924_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kelas',
            name='siswa',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kelasa', to='orm.Siswa'),
        ),
    ]
