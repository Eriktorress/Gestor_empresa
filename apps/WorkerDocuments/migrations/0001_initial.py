# Generated by Django 3.2.16 on 2023-06-22 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Worker', '0015_auto_20230621_2219'),
        ('Tipodocumento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkerDocuments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_tipo_doc', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Tipodocumento.tipodocumento')),
                ('id_worker', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Worker.worker')),
            ],
        ),
    ]