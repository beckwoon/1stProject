# Generated by Django 2.1 on 2019-11-18 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recovery', '0003_auto_20191115_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recovery',
            name='appraiser',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='반납평가사'),
        ),
        migrations.AlterField(
            model_name='recovery',
            name='cus_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='고객연락처'),
        ),
    ]
