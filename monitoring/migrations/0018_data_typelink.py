# Generated by Django 2.1 on 2019-12-02 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0017_cartypemgt'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='typelink',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='monitoring.CarTypeMgt'),
        ),
    ]
