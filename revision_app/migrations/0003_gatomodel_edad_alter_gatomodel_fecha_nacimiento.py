# Generated by Django 4.2.2 on 2023-06-23 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revision_app', '0002_rename_fecha_naciemiento_gatomodel_fecha_nacimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='gatomodel',
            name='edad',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gatomodel',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
    ]
