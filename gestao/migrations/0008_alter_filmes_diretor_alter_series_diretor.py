# Generated by Django 5.1 on 2024-08-30 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0007_alter_filmes_options_alter_grupos_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmes',
            name='diretor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='diretor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
