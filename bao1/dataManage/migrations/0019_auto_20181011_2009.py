# Generated by Django 2.0.7 on 2018-10-11 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataManage', '0018_auto_20181011_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='zyfenlei',
            field=models.IntegerField(choices=[(2, 'php'), (1, 'java'), (3, 'C++'), (0, 'python')], default=0, verbose_name='主页分类'),
        ),
        migrations.AlterField(
            model_name='ensure',
            name='state',
            field=models.IntegerField(choices=[(0, '未处理'), (2, '已处理'), (1, '处理中')], default=0, verbose_name='状态'),
        ),
    ]
