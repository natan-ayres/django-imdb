# Generated by Django 5.0.7 on 2024-08-14 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0027_series_roteirista_alter_series_diretor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='series',
            name='roteirista',
        ),
    ]
