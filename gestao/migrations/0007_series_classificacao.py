# Generated by Django 5.0.7 on 2024-08-19 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0006_alter_series_sinopse'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='classificacao',
            field=models.CharField(choices=[('Livre', 'Livre'), ('10', '10'), ('12', '12'), ('14', '14'), ('16', '16'), ('18', '18')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]
