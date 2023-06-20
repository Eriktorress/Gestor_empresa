# Generated by Django 3.2.16 on 2023-06-20 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Workplace', '0001_initial'),
        ('Generoworker', '0001_initial'),
        ('Discapacidad', '0001_initial'),
        ('Worker', '0009_alter_worker_estado_worker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='id_Discapacidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Discapacidad.discapacidad'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='id_Genworker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Generoworker.generoworker'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='id_workplace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Workplace.workplace'),
        ),
    ]
