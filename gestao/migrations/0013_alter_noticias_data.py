# Generated by Django 5.0.7 on 2024-08-05 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0012_alter_noticias_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='data',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
