# Generated by Django 2.2.7 on 2019-11-06 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empreza', '0002_auto_20191106_0225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empreza',
            name='nombre_empresa',
            field=models.CharField(default='Type here', max_length=30),
        ),
    ]