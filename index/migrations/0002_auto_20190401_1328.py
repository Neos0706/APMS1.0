# Generated by Django 2.1.7 on 2019-04-01 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': '农产品信息', 'verbose_name_plural': '农产品信息'},
        ),
        migrations.AddField(
            model_name='news',
            name='news_context',
            field=models.CharField(default='', max_length=200, verbose_name='新闻内容'),
        ),
        migrations.AlterField(
            model_name='admin',
            name='admin_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='管理员序号'),
        ),
        migrations.AlterField(
            model_name='admin',
            name='admin_level',
            field=models.CharField(max_length=20, verbose_name='管理员权限'),
        ),
        migrations.AlterField(
            model_name='admin',
            name='admin_mark',
            field=models.CharField(max_length=20, verbose_name='管理员备注'),
        ),
        migrations.AlterField(
            model_name='admin',
            name='admin_name',
            field=models.CharField(max_length=20, verbose_name='管理员账号'),
        ),
        migrations.AlterField(
            model_name='admin',
            name='admin_password',
            field=models.CharField(max_length=20, verbose_name='管理员密码'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='订单序号'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_number',
            field=models.CharField(max_length=20, verbose_name='订单数量'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_user',
            field=models.CharField(max_length=20, verbose_name='订单用户'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='新闻序号'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_mark',
            field=models.CharField(max_length=20, verbose_name='新闻内容'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_send',
            field=models.CharField(max_length=20, verbose_name='新闻发布人'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_title',
            field=models.CharField(max_length=20, verbose_name='新闻标题'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ap_area',
            field=models.CharField(max_length=20, verbose_name='农产品产地'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ap_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='农产品序号'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ap_mark',
            field=models.CharField(max_length=20, verbose_name='农产品备注'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ap_name',
            field=models.CharField(max_length=50, verbose_name='农产品名称'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ap_number',
            field=models.FloatField(max_length=20, verbose_name='农产品数量'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_book_id',
            field=models.CharField(max_length=20, verbose_name='用户订单'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='用户序号'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_level',
            field=models.CharField(max_length=20, verbose_name='用户权限'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_mark',
            field=models.CharField(max_length=20, verbose_name='用户备注'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=20, verbose_name='用户账号'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_password',
            field=models.CharField(max_length=20, verbose_name='用户密码'),
        ),
    ]
