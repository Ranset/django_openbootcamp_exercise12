# Generated by Django 4.1.3 on 2022-11-18 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directores', '0003_directores_fallecimiento_directores_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directores',
            name='fallecimiento',
            field=models.DateField(blank=True, help_text='Si sigue vivo dejar en blanco', null=True),
        ),
    ]