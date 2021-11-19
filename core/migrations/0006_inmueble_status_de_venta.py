# Generated by Django 3.2.8 on 2021-10-21 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_inmueble_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmueble',
            name='status_de_venta',
            field=models.CharField(blank=True, choices=[('pendiente', 'pendiente'), ('publicado', 'publicado'), ('finalizado', 'finalizado')], default='publicado', max_length=20, null=True),
        ),
    ]
