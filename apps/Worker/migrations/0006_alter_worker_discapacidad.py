# Generated by Django 3.2.16 on 2023-06-20 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Worker', '0005_auto_20230620_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='discapacidad',
            field=models.CharField(max_length=1, verbose_name='Es_Discapacitado'),
        ),
    ]