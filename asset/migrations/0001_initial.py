# Generated by Django 2.2.6 on 2021-07-06 05:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='カテゴリ名')),
                ('dt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='追加日')),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, verbose_name='タイトル')),
                ('comment', models.CharField(blank=True, max_length=2000, verbose_name='コメント')),
                ('income', models.IntegerField(default=0, verbose_name='収入')),
                ('spending', models.IntegerField(default=0, verbose_name='支出')),
                ('dt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='投稿日')),
                ('pay_dt', models.DateTimeField(verbose_name='決済日')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.Category', verbose_name='カテゴリ')),
            ],
            options={
                'db_table': 'balance',
            },
        ),
    ]
