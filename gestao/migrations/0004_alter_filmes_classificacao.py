# Generated by Django 5.0.7 on 2024-08-18 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0003_rename_show_reviewsfilmes_mostrar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmes',
            name='classificacao',
            field=models.CharField(choices=[('Livre', 'Livre'), ('10', '10'), ('12', '12'), ('14', '14'), ('16', '16'), ('18', '18')], max_length=20),
        ),
    ]
