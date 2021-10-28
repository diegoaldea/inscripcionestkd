# Generated by Django 3.2.8 on 2021-10-28 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20211010_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='competidor',
            name='instructor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='competidor',
            name='categoria',
            field=models.CharField(choices=[('Kids (Hasta 7 años)', 'Kids (Hasta 7 años)'), ('Infantil A (8-9 años)', 'Infantil A (8-9 años)'), ('Infantil B (10-11 años)', 'Infantil B (10-11 años)'), ('Cadete (12-13 años)', 'Cadete (12-13 años)'), ('Juvenil A (14-15 años)', 'Juvenil A (14-15 años)'), ('Juvenil B (16-17 años)', 'Juvenil B (16-17 años)'), ('Adultos (18-35 años)', 'Adultos (18-35 años)'), ('Seniors (+35 años)', 'Seniors (+35 años)')], max_length=100, verbose_name='categoría'),
        ),
        migrations.AlterField(
            model_name='competidor',
            name='graduacion',
            field=models.CharField(choices=[('Blanco - Blanco Punta Amarilla', 'Blanco - Blanco Punta Amarilla'), ('Amarillo - Verde Punta Azul', 'Amarillo - Verde Punta Azul'), ('Azul - Rojo Punta Negra', 'Azul - Rojo Punta Negra'), ('I Dan', 'I Dan'), ('II Dan', 'II Dan'), ('III Dan', 'III Dan'), ('IV Dan - VI Dan', 'IV Dan - VI Dan')], max_length=100, verbose_name='graduación'),
        ),
    ]
