# Generated by Django 2.1 on 2019-12-02 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('remgt', '0002_auto_20191202_1046'),
        ('monitoring', '0011_data_ex'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='typerink',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='remgt.CarTypeMgt'),
        ),
    ]
