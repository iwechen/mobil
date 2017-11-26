# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(verbose_name='商品名称', max_length=20)),
                ('desc', models.CharField(verbose_name='商品简介', max_length=128)),
                ('price', models.DecimalField(max_digits=10, verbose_name='商品价格', decimal_places=2)),
                ('unite', models.CharField(verbose_name='商品单位', max_length=20)),
                ('stock', models.IntegerField(default=1, verbose_name='商品库存')),
                ('sales', models.IntegerField(default=0, verbose_name='商品销量')),
                ('detail', tinymce.models.HTMLField(verbose_name='商品详情')),
                ('image', models.ImageField(upload_to='goods', verbose_name='商品图片')),
                ('status', models.SmallIntegerField(default=1, choices=[(0, '下线'), (1, '上线')], verbose_name='商品状态')),
            ],
            options={
                'verbose_name_plural': '商品',
                'db_table': 'cm_goods',
                'verbose_name': '商品',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(verbose_name='店铺名称', max_length=20)),
                ('addr', models.CharField(verbose_name='店铺地址', max_length=128)),
                ('detail', tinymce.models.HTMLField(verbose_name='商品详情')),
            ],
            options={
                'verbose_name_plural': '店铺s',
                'db_table': 'cm_shop',
                'verbose_name': '店铺s',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(verbose_name='种类名称', max_length=20)),
                ('image', models.ImageField(upload_to='goods', verbose_name='种类图片')),
            ],
            options={
                'verbose_name_plural': '种类',
                'db_table': 'cm_type',
                'verbose_name': '种类',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='shop_name',
            field=models.ForeignKey(to='cm_goods.Shop', verbose_name='所属店铺'),
        ),
        migrations.AddField(
            model_name='goods',
            name='type_id',
            field=models.ForeignKey(to='cm_goods.Type', verbose_name='商品种类'),
        ),
    ]
