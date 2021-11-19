# Generated by Django 3.2.8 on 2021-11-06 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_imageninmueble'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contanto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('correo', models.EmailField(max_length=254)),
                ('mensaje', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='imageninmueble',
            name='proyecto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.proyecto'),
        ),
    ]
