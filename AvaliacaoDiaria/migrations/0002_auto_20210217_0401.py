# Generated by Django 3.1.5 on 2021-02-17 07:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('AvaliacaoDiaria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacaodiaria',
            name='data',
            field=models.DateField(default=datetime.datetime(2021, 2, 17, 7, 1, 7, 746686, tzinfo=utc), verbose_name='Data '),
        ),
    ]