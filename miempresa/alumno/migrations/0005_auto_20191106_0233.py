# Generated by Django 2.2.7 on 2019-11-06 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0004_auto_20191106_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='numero_empleado',
            field=models.IntegerField(),
        ),
    ]
