# Generated by Django 5.1 on 2024-08-27 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0016_series_atores_series_escritor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='episodios',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
