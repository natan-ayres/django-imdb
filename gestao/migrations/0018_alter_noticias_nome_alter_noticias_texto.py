# Generated by Django 5.0.7 on 2024-08-08 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0017_alter_filmes_options_alter_noticias_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='nome',
            field=models.CharField(max_length=31),
        ),
        migrations.AlterField(
            model_name='noticias',
            name='texto',
            field=models.TextField(max_length=684),
        ),
    ]
