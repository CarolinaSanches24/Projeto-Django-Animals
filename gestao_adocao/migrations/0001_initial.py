# Generated by Django 4.2.11 on 2024-04-11 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adotante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('idade', models.IntegerField()),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('endereco', models.CharField(max_length=50)),
                ('termo_responsabilidade', models.BooleanField(default=False)),
                ('espaco', models.BooleanField(default=False)),
                ('tempo', models.BooleanField(default=False)),
                ('ciente_custos', models.BooleanField(default=False)),
                ('disposicao_fisica_emocional', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Adotante',
                'verbose_name_plural': 'Adotantes',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Adocao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('termo_aceito', models.BooleanField(default=False)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('adotante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestao_adocao.adotante')),
            ],
            options={
                'verbose_name': 'Adocao',
                'verbose_name_plural': 'Adocoes',
                'ordering': ['-data'],
            },
        ),
    ]
