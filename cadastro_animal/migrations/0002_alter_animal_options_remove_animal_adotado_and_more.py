# Generated by Django 4.2.11 on 2024-03-28 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_animal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='animal',
            options={},
        ),
        migrations.RemoveField(
            model_name='animal',
            name='adotado',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='castrado',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='data',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='doencas_existentes',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='especie',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='porte',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='raca',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='sexo',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='vacinado',
        ),
    ]
