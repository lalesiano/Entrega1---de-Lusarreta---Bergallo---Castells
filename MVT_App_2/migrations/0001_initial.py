# Generated by Django 4.1.1 on 2022-11-08 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=20)),
                ('conductor', models.CharField(max_length=50)),
                ('foto', models.ImageField(upload_to='')),
            ],
        ),
    ]
