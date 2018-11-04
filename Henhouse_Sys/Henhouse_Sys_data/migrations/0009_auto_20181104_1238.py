# Generated by Django 2.0.7 on 2018-11-04 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Henhouse_Sys_data', '0008_auto_20181103_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='notice_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('c_user', models.ForeignKey(on_delete=None, parent_link=True, related_name='c_user', to='Henhouse_Sys_data.party_user', verbose_name='发布人')),
                ('j_user', models.ForeignKey(blank=True, null=True, on_delete=None, parent_link=True, related_name='j_user', to='Henhouse_Sys_data.party_user', verbose_name='接受人')),
                ('c_time', models.CharField(max_length=32, verbose_name='创建时间')),
                ('state', models.TextField(blank=True, choices=[('1', '已读'), ('2', '未读')], null=True, verbose_name='状态')),
                ('content', models.TextField(verbose_name='内容')),
            ],
            options={
                'verbose_name': '通知信息表',
            },
        ),
        migrations.AlterField(
            model_name='company',
            name='hierarchy',
            field=models.IntegerField(choices=[(1, '畜牧中心'), (3, '养殖场'), (2, '畜牧公司'), (4, '畜舍')], verbose_name='层级'),
        ),
        migrations.AlterField(
            model_name='muen',
            name='muen_a',
            field=models.IntegerField(choices=[(1, '畜牧中心'), (3, '养殖场'), (2, '畜牧公司'), (4, '畜舍')], verbose_name='要求不低于这个权限'),
        ),
    ]
