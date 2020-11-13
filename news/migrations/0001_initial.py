# Generated by Django 2.1.7 on 2019-04-26 08:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=20, verbose_name='新闻标题')),
                ('news_context', models.CharField(max_length=200, verbose_name='新闻内容')),
                ('news_mark', models.CharField(max_length=20, verbose_name='新闻备注')),
                ('news_send', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='新闻发布人')),
            ],
            options={
                'verbose_name': '新闻信息',
                'verbose_name_plural': '新闻信息',
            },
        ),
    ]
