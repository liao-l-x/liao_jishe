# Generated by Django 2.0.7 on 2018-10-11 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataManage', '0014_auto_20181011_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user1',
            name='img',
            field=models.ImageField(upload_to='./static/user_img/', verbose_name='头像'),
        ),
    ]