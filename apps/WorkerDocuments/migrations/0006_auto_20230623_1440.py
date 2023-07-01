# Generated by Django 3.2.16 on 2023-06-23 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tipodocumento', '0001_initial'),
        ('Worker', '0015_auto_20230621_2219'),
        ('WorkerDocuments', '0005_alter_workerdocuments_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='workerdocuments',
            name='id_tipo_doc',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Tipodocumento.tipodocumento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workerdocuments',
            name='id_worker',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Worker.worker'),
            preserve_default=False,
        ),
    ]