# Generated by Django 5.1 on 2024-08-28 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0005_grupos_qntdmembros'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupos',
            name='qntdmembros',
            field=models.IntegerField(default=0),
        ),
    ]
