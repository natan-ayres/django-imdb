# Generated by Django 5.0.7 on 2024-08-08 13:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0019_noticias_mostrar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='nome',
            field=models.CharField(max_length=31, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
        migrations.AlterField(
            model_name='noticias',
            name='texto',
            field=models.TextField(max_length=684, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]
