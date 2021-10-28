from django.db import models
from django.db.models.fields import CharField, IntegerField

class Competidor(models.Model):
    categoriaChoices = (
        ('Kids (Hasta 7 años)', 'Kids (Hasta 7 años)'),
        ('Infantil A (8-9 años)', 'Infantil A (8-9 años)'),
        ('Infantil B (10-11 años)', 'Infantil B (10-11 años)'),
        ('Cadete (12-13 años)', 'Cadete (12-13 años)'),
        ('Juvenil A (14-15 años)', 'Juvenil A (14-15 años)'),
        ('Juvenil B (16-17 años)', 'Juvenil B (16-17 años)'),
        ('Adultos (18-35 años)', 'Adultos (18-35 años)'),
        ('Seniors (+35 años)', 'Seniors (+35 años)')
    )

    graduacionChoices = (
        ('Blanco - Blanco Punta Amarilla', 'Blanco - Blanco Punta Amarilla'),
        ('Amarillo - Verde Punta Azul', 'Amarillo - Verde Punta Azul'),
        ('Azul - Rojo Punta Negra', 'Azul - Rojo Punta Negra'),
        ('I Dan', 'I Dan'),
        ('II Dan', 'II Dan'),
        ('III Dan', 'III Dan'),
        ('IV Dan - VI Dan', 'IV Dan - VI Dan')
    )

    nombre = CharField(max_length=30, null = False, blank = False)
    apellido = CharField(max_length=30, null = False, blank = False)
    categoria = CharField(max_length=100, verbose_name="categoría", null = False, blank = False, choices = categoriaChoices)
    graduacion = CharField(max_length=100, verbose_name="graduación", null = False, blank = False, choices = graduacionChoices)
    academia = CharField(max_length = 100, null = False, blank = False)
    instructor = CharField(max_length=100, null = False, blank = False)
    celular = IntegerField(null = False, blank = False)
    dni = IntegerField(unique = True, null = False, blank = False)

    def __str__(self) -> str:
        return self.nombre + " " + self.apellido + " /// " + self.academia
    class Meta:
        verbose_name = "Competidor"
        verbose_name_plural = "Competidores"
    