# Generated by Django 2.1.1 on 2018-09-26 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0007_auto_20180926_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='device_status_id',
            field=models.IntegerField(choices=[(1, '上架'), (2, '在线'), (3, '离线'), (4, '下架')], default=1, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='device_type_id',
            field=models.IntegerField(choices=[('register', '注册'), ('forget', '找回密码')], verbose_name='资产类型'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='latest_date',
            field=models.DateField(null=True, verbose_name='最后更新时间'),
        ),
        migrations.AlterField(
            model_name='server',
            name='hostname',
            field=models.CharField(max_length=128, unique=True, verbose_name='名称'),
        ),
    ]
