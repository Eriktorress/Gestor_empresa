# Generated by Django 3.2.16 on 2023-07-02 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Company', '0002_company'),
        ('Maintainers', '0002_comuna_discapacidad_estado_region_sexo_tipodiscapacidad_tipodocumento'),
        ('Workplace', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workplace',
            fields=[
                ('id_workplace', models.AutoField(primary_key=True, serialize=False)),
                ('name_workplace', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('comuna', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Maintainers.comuna', verbose_name='Comuna')),
                ('estado_workplace', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Maintainers.estado')),
                ('id_company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Company.company')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Maintainers.region', verbose_name='Región')),
            ],
        ),
    ]
