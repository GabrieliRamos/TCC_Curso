# Generated by Django 3.1.5 on 2021-02-11 23:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('AvaliacaoDiaria', '0003_avaliacaodiaria_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacaodiaria',
            name='data',
            field=models.DateField(default=datetime.datetime(2021, 2, 11, 23, 56, 21, 947278, tzinfo=utc), verbose_name='Data '),
        ),
    ]
