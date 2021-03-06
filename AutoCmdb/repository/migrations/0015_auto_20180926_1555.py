# Generated by Django 2.1.1 on 2018-09-26 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0014_auto_20180926_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disk',
            name='server_obj',
        ),
        migrations.RemoveField(
            model_name='memory',
            name='server_obj',
        ),
        migrations.AlterModelOptions(
            name='networkdevice',
            options={'verbose_name_plural': '网络设备表'},
        ),
        migrations.AlterModelOptions(
            name='server',
            options={'verbose_name_plural': '服务器信息表'},
        ),
        migrations.AddField(
            model_name='server',
            name='capacity_disk',
            field=models.FloatField(blank=True, null=True, verbose_name='磁盘容量GB'),
        ),
        migrations.AddField(
            model_name='server',
            name='capacity_memory',
            field=models.FloatField(blank=True, null=True, verbose_name='容量'),
        ),
        migrations.AddField(
            model_name='server',
            name='pd_type',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='磁盘类型'),
        ),
        migrations.AlterField(
            model_name='server',
            name='hostname',
            field=models.CharField(max_length=128, unique=True, verbose_name='主机名称'),
        ),
        migrations.DeleteModel(
            name='Disk',
        ),
        migrations.DeleteModel(
            name='Memory',
        ),
    ]
