# Generated by Django 2.1.1 on 2018-09-26 04:01

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('phone', models.CharField(max_length=32, verbose_name='座机')),
                ('mobile', models.CharField(max_length=32, verbose_name='手机')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户表',
                'verbose_name_plural': '用户表',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AdminInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('user_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '管理员表',
            },
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_type_id', models.IntegerField(choices=[(1, '服务器'), (2, '交换机'), (3, '防火墙')], default=1)),
                ('device_status_id', models.IntegerField(choices=[(1, '上架'), (2, '在线'), (1, '离线'), (1, '下架')], default=1)),
                ('cabinet_num', models.CharField(blank=True, max_length=32, null=True, verbose_name='机柜号')),
                ('cabinet_order', models.CharField(blank=True, max_length=30, null=True, verbose_name='机柜中序号')),
                ('lastest_date', models.DateField(null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '资产表',
            },
        ),
        migrations.CreateModel(
            name='AssetRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('asset_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ar', to='repository.Asset')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '资产记录表',
            },
        ),
        migrations.CreateModel(
            name='BusinessUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='业务线')),
            ],
            options={
                'verbose_name_plural': '业务线表',
            },
        ),
        migrations.CreateModel(
            name='Disk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot', models.CharField(max_length=8, verbose_name='插槽位')),
                ('model', models.CharField(max_length=32, verbose_name='磁盘型号')),
                ('capacity', models.FloatField(verbose_name='磁盘容量GB')),
                ('pd_type', models.CharField(max_length=32, verbose_name='磁盘类型')),
            ],
            options={
                'verbose_name_plural': '硬盘表',
            },
        ),
        migrations.CreateModel(
            name='ErrorLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16)),
                ('content', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('asset_obj', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='repository.Asset')),
            ],
            options={
                'verbose_name_plural': '错误日志表',
            },
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='机房')),
                ('floor', models.IntegerField(default=1, verbose_name='楼层')),
            ],
            options={
                'verbose_name_plural': '机房表',
            },
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot', models.CharField(max_length=32, verbose_name='插槽位')),
                ('manufacturer', models.CharField(blank=True, max_length=32, null=True, verbose_name='制作商')),
                ('model', models.CharField(max_length=64, verbose_name='型号')),
                ('capacity', models.FloatField(blank=True, null=True, verbose_name='容量')),
                ('sn', models.CharField(blank=True, max_length=64, null=True, verbose_name='内存SN号')),
                ('speed', models.CharField(blank=True, max_length=16, null=True, verbose_name='速度')),
            ],
            options={
                'verbose_name_plural': '内存表',
            },
        ),
        migrations.CreateModel(
            name='NetworkDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('management_ip', models.CharField(blank=True, max_length=64, null=True, verbose_name='管理IP')),
                ('vlan_ip', models.CharField(blank=True, max_length=64, null=True, verbose_name='VlanIP')),
                ('intranet_ip', models.CharField(blank=True, max_length=128, null=True, verbose_name='内网IP')),
                ('sn', models.CharField(max_length=64, unique=True, verbose_name='SN号')),
                ('manufacture', models.CharField(blank=True, max_length=128, null=True, verbose_name='制作商')),
                ('model', models.CharField(blank=True, max_length=128, null=True, verbose_name='型号')),
                ('port_num', models.SmallIntegerField(blank=True, null=True, verbose_name='端口个数')),
                ('device_detail', models.CharField(blank=True, max_length=255, null=True, verbose_name='设置详细配置')),
                ('asset', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='repository.Asset')),
            ],
            options={
                'verbose_name_plural': '网络设备',
            },
        ),
        migrations.CreateModel(
            name='NIC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='网卡名称')),
                ('hwaddr', models.CharField(max_length=64, verbose_name='网卡mac地址')),
                ('netmask', models.CharField(max_length=64)),
                ('ipaddrs', models.CharField(max_length=256, verbose_name='ip地址')),
                ('up', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': '网卡表',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=128, unique=True)),
                ('sn', models.CharField(db_index=True, max_length=64, verbose_name='SN号')),
                ('manufacturer', models.CharField(blank=True, max_length=64, null=True, verbose_name='制作商')),
                ('model', models.CharField(blank=True, max_length=64, null=True, verbose_name='型号')),
                ('manage_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='管理IP')),
                ('os_platfrom', models.CharField(blank=True, max_length=16, null=True, verbose_name='系统')),
                ('os_version', models.CharField(blank=True, max_length=16, null=True, verbose_name='系统版本')),
                ('cpu_count', models.IntegerField(blank=True, null=True, verbose_name='CPU个数')),
                ('cpu_physical_count', models.IntegerField(blank=True, null=True, verbose_name='CPU物理个数')),
                ('cpu_model', models.CharField(blank=True, max_length=128, null=True, verbose_name='CPU型号')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('asset', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='repository.Asset')),
            ],
            options={
                'verbose_name_plural': '服务器表',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='标签')),
            ],
            options={
                'verbose_name_plural': '标签表',
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '用户组表',
            },
        ),
        migrations.AddField(
            model_name='nic',
            name='server_obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nic', to='repository.Server'),
        ),
        migrations.AddField(
            model_name='memory',
            name='server_obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memory', to='repository.Server'),
        ),
        migrations.AddField(
            model_name='disk',
            name='server_obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disk', to='repository.Server'),
        ),
        migrations.AddField(
            model_name='businessunit',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='c', to='repository.UserGroup', verbose_name='业务线联系人'),
        ),
        migrations.AddField(
            model_name='businessunit',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='m', to='repository.UserGroup', verbose_name='系统管理员'),
        ),
        migrations.AddField(
            model_name='asset',
            name='business_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='repository.BusinessUnit', verbose_name='属于的业务线'),
        ),
        migrations.AddField(
            model_name='asset',
            name='idc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='repository.IDC', verbose_name='IDC机房'),
        ),
        migrations.AddField(
            model_name='asset',
            name='tag',
            field=models.ManyToManyField(to='repository.Tag'),
        ),
    ]
