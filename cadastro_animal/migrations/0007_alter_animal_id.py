# Generated by Django 4.2.11 on 2024-03-29 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_animal', '0006_alter_animal_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
