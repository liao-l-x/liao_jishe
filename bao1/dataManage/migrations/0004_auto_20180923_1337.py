# Generated by Django 2.0.7 on 2018-09-23 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataManage', '0003_auto_20180923_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ensure',
            name='state',
            field=models.IntegerField(choices=[(1, '处理中'), (0, '未处理'), (2, '已处理')], default=0, verbose_name='状态'),
        ),
    ]