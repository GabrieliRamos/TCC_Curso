# Generated by Django 3.1.5 on 2021-02-16 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cirurgias', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cirurgias',
            options={'ordering': ('-data_cirurgia',)},
        ),
    ]
