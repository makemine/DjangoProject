# Generated by Django 2.1.1 on 2018-09-26 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0006_auto_20180926_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='device_status_id',
            field=models.IntegerField(choices=[(1, '上架'), (2, '在线'), (1, '离线'), (1, '下架')], default=1),
        ),
        migrations.AlterField(
            model_name='asset',
            name='device_type_id',
            field=models.IntegerField(choices=[(1, '服务器'), (2, '交换机'), (3, '防火墙')], default=1),
        ),
    ]