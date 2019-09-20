# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-11-24 15:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('notas', '0001_initial'),
        ('docentes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CuartoNTPL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.PositiveSmallIntegerField()),
                ('descripcion', models.CharField(max_length=140)),
                ('valor', models.PositiveSmallIntegerField()),
                ('alumno_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.PdoEscAlum')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.MateriaMaestro')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.Maestro')),
            ],
        ),
        migrations.CreateModel(
            name='CuartoNTSL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.PositiveSmallIntegerField()),
                ('descripcion', models.CharField(max_length=140)),
                ('valor', models.PositiveSmallIntegerField()),
                ('alumno_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.PdoEscAlum')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.MateriaMaestro')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.Maestro')),
            ],
        ),
        migrations.CreateModel(
            name='CuartoNTTL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.PositiveSmallIntegerField()),
                ('descripcion', models.CharField(max_length=140)),
                ('valor', models.PositiveSmallIntegerField()),
                ('alumno_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.PdoEscAlum')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.MateriaMaestro')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.Maestro')),
            ],
        ),
        migrations.CreateModel(
            name='PrimeroNTPL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.PositiveSmallIntegerField()),
                ('descripcion', models.CharField(max_length=140)),
                ('valor', models.PositiveSmallIntegerField()),
                ('alumno_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.PdoEscAlum')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.MateriaMaestro')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.Maestro')),
            ],
        ),
        migrations.CreateModel(
            name='PrimeroNTSL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.PositiveSmallIntegerField()),
                ('descripcion', models.CharField(max_length=140)),
                ('valor', models.PositiveSmallIntegerField()),
                ('alumno_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.PdoEscAlum')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.MateriaMaestro')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.Maestro')),
            ],
        ),
        migrations.CreateModel(
            name='PrimeroNTTL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.PositiveSmallIntegerField()),
                ('descripcion', models.CharField(max_length=140)),
                ('valor', models.PositiveSmallIntegerField()),
                ('alumno_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.PdoEscAlum')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.MateriaMaestro')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.Maestro')),
            ],
        ),
        migrations.CreateModel(
            name='QuintoNTPL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.PositiveSmallIntegerField()),
                ('descripcion', models.CharField(max_length=140)),
                ('valor', models.PositiveSmallIntegerField()),
                ('alumno_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.PdoEscAlum')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.MateriaMaestro')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.Maestro')),
            ],
        ),
        migrations.CreateModel(
            name='QuintoNTSL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.PositiveSmallIntegerField()),
                ('descripcion', models.CharField(max_length=140)),
                ('valor', models.PositiveSmallIntegerField()),
                ('alumno_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.PdoEscAlum')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.MateriaMaestro')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.Maestro')),
            ],
        ),
        migrations.CreateModel(
            name='QuintoNTTL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.PositiveSmallIntegerField()),
                ('descripcion', models.CharField(max_length=140)),
                ('valor', models.PositiveSmallIntegerField()),
                ('alumno_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.PdoEscAlum')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.MateriaMaestro')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.Maestro')),
            ],
        ),
        migrations.CreateModel(
            name='SegundoNTPL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.PositiveSmallIntegerField()),
                ('descripcion', models.CharField(max_length=140)),
                ('valor', models.PositiveSmallIntegerField()),
                ('alumno_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.PdoEscAlum')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.MateriaMaestro')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.Maestro')),
            ],
        ),
        migrations.CreateModel(
            name='SegundoNTSL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.PositiveSmallIntegerField()),
                ('descripcion', models.CharField(max_length=140)),
                ('valor', models.PositiveSmallIntegerField()),
                ('alumno_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.PdoEscAlum')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.MateriaMaestro')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.Maestro')),
            ],
        ),
        migrations.CreateModel(
            name='SegundoNTTL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.PositiveSmallIntegerField()),
                ('descripcion', models.CharField(max_length=140)),
                ('valor', models.PositiveSmallIntegerField()),
                ('alumno_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.PdoEscAlum')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.MateriaMaestro')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.Maestro')),
            ],
        ),
        migrations.CreateModel(
            name='TercerNTPL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.PositiveSmallIntegerField()),
                ('descripcion', models.CharField(max_length=140)),
                ('valor', models.PositiveSmallIntegerField()),
                ('alumno_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.PdoEscAlum')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.MateriaMaestro')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.Maestro')),
            ],
        ),
        migrations.CreateModel(
            name='TercerNTSL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.PositiveSmallIntegerField()),
                ('descripcion', models.CharField(max_length=140)),
                ('valor', models.PositiveSmallIntegerField()),
                ('alumno_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.PdoEscAlum')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.MateriaMaestro')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.Maestro')),
            ],
        ),
        migrations.CreateModel(
            name='TercerNTTL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.PositiveSmallIntegerField()),
                ('descripcion', models.CharField(max_length=140)),
                ('valor', models.PositiveSmallIntegerField()),
                ('alumno_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.PdoEscAlum')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.MateriaMaestro')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.Maestro')),
            ],
        ),
    ]
