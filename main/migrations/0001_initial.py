# Generated by Django 5.2.1 on 2025-05-07 15:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('album', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('album_art', models.URLField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Themes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youtube_link', models.URLField(max_length=500)),
                ('spotify_link', models.URLField(max_length=500)),
                ('apple_music_link', models.URLField(max_length=500)),
                ('recommendation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.recommendations')),
            ],
        ),
        migrations.AddField(
            model_name='recommendations',
            name='themes',
            field=models.ManyToManyField(blank=True, max_length=100, null=True, to='main.themes'),
        ),
    ]
