# Generated by Django 4.1.2 on 2022-10-12 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MVT_App', '0002_persona_fecha_ingreso'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Humanos',
            new_name='Persona',
        ),
    ]
