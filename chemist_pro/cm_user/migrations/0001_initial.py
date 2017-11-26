# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('username', models.CharField(verbose_name='用户名', default='90419120', max_length=20)),
                ('password', models.CharField(verbose_name='密码', max_length=40)),
                ('tel', models.CharField(verbose_name='电话号码', max_length=20)),
                ('email', models.EmailField(verbose_name='邮箱', max_length=254)),
                ('is_shop', models.BooleanField(verbose_name='店铺状态', default=False)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'cm_user',
            },
        ),
    ]
