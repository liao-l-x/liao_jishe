# Generated by Django 2.0.7 on 2018-09-25 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataManage', '0008_auto_20180924_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='zyfenlei',
            field=models.IntegerField(choices=[('0', 'python'), ('1', 'java'), ('2', 'php'), ('3', 'C++')], default=0, verbose_name='主页分类'),
        ),
    ]
