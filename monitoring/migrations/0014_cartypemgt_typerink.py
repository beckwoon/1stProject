# Generated by Django 2.1 on 2019-12-02 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0013_auto_20191202_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartypemgt',
            name='typerink',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='monitoring.Data'),
        ),
    ]
