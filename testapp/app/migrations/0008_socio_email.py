# Generated by Django 3.2.7 on 2023-06-07 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_socio_ruc'),
    ]

    operations = [
        migrations.AddField(
            model_name='socio',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
