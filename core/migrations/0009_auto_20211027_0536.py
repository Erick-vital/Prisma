# Generated by Django 3.2.8 on 2021-10-27 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_inmueble_dias_publicado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispositivo_id', models.CharField(max_length=300)),
            ],
        ),
        migrations.RemoveField(
            model_name='favorito',
            name='device',
        ),
        migrations.AddField(
            model_name='favorito',
            name='dispositivo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.dispositivo'),
        ),
    ]
