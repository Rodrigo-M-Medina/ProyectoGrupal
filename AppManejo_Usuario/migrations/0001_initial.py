# Generated by Django 4.1.3 on 2022-12-20 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=25)),
                ('subtitulo', models.CharField(max_length=25)),
                ('cuerpo', models.CharField(max_length=1000)),
                ('autor', models.CharField(max_length=20)),
                ('img', models.ImageField(upload_to=None)),
            ],
        ),
    ]
