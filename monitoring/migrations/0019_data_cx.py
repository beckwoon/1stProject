# Generated by Django 2.1 on 2019-12-04 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0018_data_typelink'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='cx',
            field=models.BooleanField(default=False, verbose_name='인증대상'),
        ),
    ]
