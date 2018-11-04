# Generated by Django 2.0.7 on 2018-09-25 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataManage', '0009_auto_20180925_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='label_id',
            field=models.ManyToManyField(related_name='article_label', related_query_name='article_label', to='dataManage.label', verbose_name='文章标签'),
        ),
        migrations.AlterField(
            model_name='article',
            name='zyfenlei',
            field=models.IntegerField(choices=[(2, 'php'), (0, 'python'), (1, 'java'), (3, 'C++')], default=0, verbose_name='主页分类'),
        ),
        migrations.AlterField(
            model_name='ensure',
            name='state',
            field=models.IntegerField(choices=[(0, '未处理'), (2, '已处理'), (1, '处理中')], default=0, verbose_name='状态'),
        ),
    ]