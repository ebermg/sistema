# Generated by Django 4.0.3 on 2022-04-20 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libreria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, verbose_name='Nombre libro')),
                ('descripcion', models.CharField(blank=True, max_length=100, verbose_name='Descripcion del libro')),
            ],
        ),
    ]