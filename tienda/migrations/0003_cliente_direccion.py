# Generated by Django 3.2.6 on 2021-08-05 17:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_cliente_comprobante_detallecomprobante'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(default=datetime.date, max_length=100),
            preserve_default=False,
        ),
    ]
