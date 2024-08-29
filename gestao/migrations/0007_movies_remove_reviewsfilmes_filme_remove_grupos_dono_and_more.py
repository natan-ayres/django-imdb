# Generated by Django 5.1 on 2024-08-29 12:53

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0006_alter_grupos_qntdmembros'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('director', models.CharField(blank=True, max_length=30, null=True)),
                ('writer', models.TextField(blank=True, max_length=200, null=True)),
                ('actors', models.TextField(blank=True, max_length=200, null=True)),
                ('runtime', models.TimeField(blank=True, null=True)),
                ('rating', models.CharField(blank=True, choices=[('Livre', 'Livre'), ('10', '10'), ('12', '12'), ('14', '14'), ('16', '16'), ('18', '18')], max_length=20, null=True)),
                ('plot', models.TextField(blank=True, max_length=400, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('grade_avg', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('poster', models.ImageField(blank=True, max_length=200, null=True, upload_to='movies/')),
            ],
            options={
                'verbose_name': 'Movie',
            },
        ),
        migrations.RemoveField(
            model_name='reviewsfilmes',
            name='filme',
        ),
        migrations.RemoveField(
            model_name='grupos',
            name='dono',
        ),
        migrations.RemoveField(
            model_name='grupos',
            name='membros',
        ),
        migrations.RemoveField(
            model_name='grupos',
            name='waitlist',
        ),
        migrations.RemoveField(
            model_name='noticias',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='reviewsfilmes',
            name='usuario',
        ),
        migrations.RenameField(
            model_name='reviewsseries',
            old_name='data',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='reviewsseries',
            old_name='nota',
            new_name='grade',
        ),
        migrations.RenameField(
            model_name='reviewsseries',
            old_name='mostrar',
            new_name='show',
        ),
        migrations.RenameField(
            model_name='reviewsseries',
            old_name='usuario',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='atores',
            new_name='actors',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='data',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='data_termino',
            new_name='date_end',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='diretor',
            new_name='director',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='episodios',
            new_name='episodes',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='nota_media',
            new_name='grade_avg',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='nome',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='sinopse',
            new_name='plot',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='classificacao',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='avaliacoes',
            new_name='reviews',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='temporadas',
            new_name='seasons',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='escritor',
            new_name='writer',
        ),
        migrations.AlterField(
            model_name='reviewsseries',
            name='serie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewsserie', to='gestao.series'),
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, upload_to='groups/')),
                ('desc', models.TextField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('countmembers', models.IntegerField(default=0)),
                ('members', models.ManyToManyField(blank=True, related_name='members', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('waitlist', models.ManyToManyField(blank=True, related_name='waitlist', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Group',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31, validators=[django.core.validators.MinLengthValidator(5)])),
                ('image', models.ImageField(blank=True, upload_to='news/')),
                ('text', models.TextField(max_length=684, validators=[django.core.validators.MinLengthValidator(5)])),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('show', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'News',
            },
        ),
        migrations.CreateModel(
            name='ReviewsMovies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('review', models.TextField(max_length=250)),
                ('grade', models.FloatField(validators=[django.core.validators.MinValueValidator(0, 0), django.core.validators.MaxValueValidator(10, 0)])),
                ('show', models.BooleanField(default=False)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewsmovie', to='gestao.movies')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Review - Movie',
            },
        ),
        migrations.AddField(
            model_name='movies',
            name='reviews',
            field=models.ManyToManyField(through='gestao.ReviewsMovies', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Filmes',
        ),
        migrations.DeleteModel(
            name='Grupos',
        ),
        migrations.DeleteModel(
            name='Noticias',
        ),
        migrations.DeleteModel(
            name='ReviewsFilmes',
        ),
    ]
