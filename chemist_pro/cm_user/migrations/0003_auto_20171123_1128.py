# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cm_user', '0002_auto_20171121_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passport',
            name='username',
            field=models.CharField(default='77036119', verbose_name='用户名', max_length=20),
        ),
    ]
