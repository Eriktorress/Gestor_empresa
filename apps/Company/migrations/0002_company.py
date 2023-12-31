# Generated by Django 3.2.16 on 2023-07-02 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Maintainers', '0002_comuna_discapacidad_estado_region_sexo_tipodiscapacidad_tipodocumento'),
        ('Company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id_company', models.AutoField(primary_key=True, serialize=False)),
                ('name_company', models.CharField(max_length=50)),
                ('rut_company', models.CharField(max_length=9)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('comuna', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Maintainers.comuna', verbose_name='Comuna')),
                ('estado_company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Maintainers.estado')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Maintainers.region', verbose_name='Región')),
            ],
        ),
    ]
