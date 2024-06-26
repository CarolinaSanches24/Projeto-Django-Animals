# Generated by Django 4.2.11 on 2024-04-03 22:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('idade', models.CharField(max_length=20)),
                ('foto', models.ImageField(upload_to='')),
                ('especie', models.CharField(choices=[('cachorro', 'Cachorro'), ('gato', 'Gato')], max_length=10, null=True)),
                ('raca', models.CharField(max_length=20, null=True)),
                ('porte', models.CharField(max_length=10, null=True)),
                ('sexo', models.CharField(choices=[('macho', 'Macho'), ('femea', 'Femea')], max_length=10, null=True)),
                ('castrado', models.BooleanField(default=False)),
                ('vacinado', models.BooleanField(default=False)),
                ('doencas_existentes', models.TextField(blank=True)),
                ('adotado', models.BooleanField(default=False)),
                ('data', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'Cadastro de animais',
            },
        ),
    ]
