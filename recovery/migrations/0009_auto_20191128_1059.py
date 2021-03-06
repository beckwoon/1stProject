# Generated by Django 2.1 on 2019-11-28 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recovery', '0008_recovery_car_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recoverymgt',
            name='receive1',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='입금액1'),
        ),
        migrations.AlterField(
            model_name='recoverymgt',
            name='receive2',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='입금액2'),
        ),
        migrations.AlterField(
            model_name='recoverymgt',
            name='receive3',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='입금액3'),
        ),
        migrations.AlterField(
            model_name='recoverymgt',
            name='receive4',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='입금액4'),
        ),
        migrations.AlterField(
            model_name='recoverymgt',
            name='receive5',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='입금액5'),
        ),
    ]
