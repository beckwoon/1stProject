# Generated by Django 2.1 on 2019-12-04 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0019_data_cx'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='cus_ctn',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
