# Generated by Django 2.0.13 on 2019-04-06 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20190406_2117'),
        ('client', '0003_remove_requestclient_dron'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestclient',
            name='promise',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='stock.Promise'),
        ),
        migrations.AlterField(
            model_name='requestclient',
            name='progress',
            field=models.IntegerField(choices=[(1, 'Заказ получен'), (2, 'В пути'), (3, 'Заказ готов к выдаче'), (4, 'Ожидает подтверждения'), (5, 'Заказ доставлен')]),
        ),
    ]
