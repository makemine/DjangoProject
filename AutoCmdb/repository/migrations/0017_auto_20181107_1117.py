# Generated by Django 2.1.1 on 2018-11-07 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0016_auto_20181106_1817'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='permission',
            options={'permissions': (('views_data', '资产表'), ('views_ops', '运维操作')), 'verbose_name': '权限表', 'verbose_name_plural': '权限表'},
        ),
    ]
