# Generated by Django 3.2.16 on 2023-06-22 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipodocumento',
            fields=[
                ('id_tipo_doc', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40, verbose_name='Descripcion')),
            ],
        ),
    ]
