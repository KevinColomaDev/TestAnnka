# Generated by Django 3.2.7 on 2023-06-07 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('compania', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('cedula', models.CharField(max_length=10)),
                ('ruc', models.CharField(max_length=13)),
                ('ciudad', models.CharField(max_length=100)),
                ('provincia', models.CharField(max_length=100)),
            ],
        ),
    ]
