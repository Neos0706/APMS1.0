# Generated by Django 2.1.7 on 2019-03-27 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('admin_name', models.CharField(max_length=20)),
                ('admin_password', models.CharField(max_length=20)),
                ('admin_level', models.CharField(max_length=20)),
                ('admin_mark', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('book_user', models.CharField(max_length=20)),
                ('book_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('news_id', models.AutoField(primary_key=True, serialize=False)),
                ('news_title', models.CharField(max_length=20)),
                ('news_send', models.CharField(max_length=20)),
                ('news_mark', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('ap_id', models.AutoField(primary_key=True, serialize=False)),
                ('ap_name', models.CharField(max_length=50)),
                ('ap_number', models.FloatField(max_length=20)),
                ('ap_area', models.CharField(max_length=20)),
                ('ap_mark', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=20)),
                ('user_password', models.CharField(max_length=20)),
                ('user_level', models.CharField(max_length=20)),
                ('user_mark', models.CharField(max_length=20)),
                ('user_book_id', models.CharField(max_length=20)),
            ],
        ),
    ]
