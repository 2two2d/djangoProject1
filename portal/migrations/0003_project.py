# Generated by Django 3.2.16 on 2022-10-15 02:46

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_alter_user_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('name', models.CharField(max_length=100, verbose_name='Project name')),
                ('description', models.TextField(max_length=400, verbose_name='Description')),
                ('img', models.ImageField(upload_to='img', verbose_name='picture')),
                ('apply_date', models.DateTimeField(default=datetime.datetime(2022, 10, 15, 9, 46, 9, 779879), editable=False)),
                ('process_status', models.CharField(blank=True, choices=[('i', 'In process'), ('d', 'done')], default='i', help_text='Status of project', max_length=1)),
                ('type_status', models.CharField(blank=True, choices=[('f', '2D design'), ('v', '3D design'), ('s', 'Sketch')], default='f', max_length=1)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Project owner')),
            ],
        ),
    ]