# Generated by Django 4.2.11 on 2024-04-11 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_animal', '0009_alter_animal_id'),
        ('gestao_adocao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adotante',
            name='animal_adotado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cadastro_animal.animal'),
        ),
    ]
