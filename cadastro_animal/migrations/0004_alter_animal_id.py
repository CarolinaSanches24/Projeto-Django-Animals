# Generated by Django 4.2.11 on 2024-03-29 01:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_animal', '0003_alter_animal_idade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]