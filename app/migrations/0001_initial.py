# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-29 15:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=256, verbose_name='Temat')),
                ('content', models.TextField(null=True)),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PresenceList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('present', models.NullBooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='SchoolSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('teacher_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('school_class', models.IntegerField(choices=[(1, '1a'), (2, '1b'), (3, '2a'), (4, '2b'), (5, '3a'), (6, '3b')], verbose_name='Klasa')),
                ('year_of_birth', models.IntegerField(blank=True, null=True, verbose_name='Rok urodzenia')),
                ('suspended', models.BooleanField(default=False, verbose_name='Zawieszony')),
            ],
            options={
                'verbose_name_plural': 'Studenci',
                'verbose_name': 'Student',
            },
        ),
        migrations.CreateModel(
            name='StudentGrades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.FloatField(choices=[(1, '1'), (1.5, '1+'), (1.75, '2-'), (2, '2'), (2.5, '2+'), (2.75, '3-'), (3, '3'), (3.5, '3+'), (3.75, '4-'), (4, '4'), (4.5, '4+'), (4.75, '5-'), (5, '5'), (5.5, '5+'), (5.75, '6-'), (6, '6')])),
                ('school_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.SchoolSubject')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='grades',
            field=models.ManyToManyField(through='app.StudentGrades', to='app.SchoolSubject'),
        ),
        migrations.AddField(
            model_name='presencelist',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student'),
        ),
        migrations.AddField(
            model_name='message',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student'),
        ),
        migrations.AddField(
            model_name='message',
            name='to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.SchoolSubject'),
        ),
    ]
