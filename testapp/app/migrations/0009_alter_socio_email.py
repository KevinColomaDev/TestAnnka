# Generated by Django 3.2.7 on 2023-06-08 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_socio_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socio',
            name='email',
            field=models.CharField(max_length=1000),
        ),
    ]