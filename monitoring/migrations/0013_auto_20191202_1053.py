# Generated by Django 2.1 on 2019-12-02 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0012_data_typerink'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarTypeMgt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartype', models.CharField(max_length=10, null=True, verbose_name='차종')),
                ('maxprice', models.IntegerField(blank=True, default=0, null=True, verbose_name='보험수리 기준금액')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='등록일자')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='수정일자')),
            ],
            options={
                'verbose_name': '차종관리',
                'verbose_name_plural': '차종관리',
                'ordering': ['created'],
            },
        ),
        migrations.RemoveField(
            model_name='data',
            name='typerink',
        ),
    ]
