# Generated by Django 3.2.16 on 2023-06-23 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorkerDocuments', '0004_auto_20230623_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workerdocuments',
            name='descripcion',
            field=models.TextField(default=1, verbose_name='Descripción'),
            preserve_default=False,
        ),
    ]
