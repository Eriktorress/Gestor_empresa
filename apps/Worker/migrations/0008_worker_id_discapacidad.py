# Generated by Django 3.2.16 on 2023-06-20 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Discapacidad', '0001_initial'),
        ('Worker', '0007_remove_worker_discapacidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='id_Discapacidad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Discapacidad.discapacidad'),
        ),
    ]