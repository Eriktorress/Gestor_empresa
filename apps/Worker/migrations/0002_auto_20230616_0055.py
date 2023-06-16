# Generated by Django 3.2.16 on 2023-06-16 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Worker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='adress',
            field=models.CharField(max_length=50, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='comuna',
            field=models.CharField(max_length=20, verbose_name='Comuna'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='lastname',
            field=models.CharField(max_length=40, verbose_name='Apellidos'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Nombres'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='phone',
            field=models.CharField(max_length=10, verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='region',
            field=models.CharField(max_length=20, verbose_name='Región'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='rut',
            field=models.CharField(max_length=9, verbose_name='RUT'),
        ),
    ]
