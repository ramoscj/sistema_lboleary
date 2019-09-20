# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-11-28 14:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0002_materia_horas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datosalumno',
            name='alumno',
        ),
        migrations.RemoveField(
            model_name='represenalumno',
            name='alumno',
        ),
        migrations.AlterField(
            model_name='materia',
            name='horas',
            field=models.PositiveIntegerField(choices=[(0, 'Seleccione'), (1, '1 Hr'), (2, '2 Hrs'), (3, '3 Hrs'), (4, '4 Hrs'), (5, '5 Hrs'), (6, '6 Hrs'), (7, '7 Hrs')], default=0),
        ),
        migrations.AlterField(
            model_name='pdoescalum',
            name='alumno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.Alumno'),
        ),
        migrations.DeleteModel(
            name='Alumno',
        ),
        migrations.DeleteModel(
            name='DatosAlumno',
        ),
        migrations.DeleteModel(
            name='RepresenAlumno',
        ),
    ]
