# Generated by Django 2.0.7 on 2018-11-04 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Henhouse_Sys_data', '0009_auto_20181104_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice_info',
            name='state',
            field=models.TextField(blank=True, choices=[('2', '未读'), ('1', '已读')], default='2', null=True, verbose_name='状态'),
        ),
    ]
