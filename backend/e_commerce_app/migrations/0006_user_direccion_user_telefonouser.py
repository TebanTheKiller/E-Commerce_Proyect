# Generated by Django 4.2.5 on 2023-11-04 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce_app', '0005_producto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='direccion',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='telefonoUser',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
