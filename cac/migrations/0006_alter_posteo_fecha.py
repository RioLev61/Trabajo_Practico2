# Generated by Django 3.2.14 on 2022-12-04 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cac', '0005_auto_20221204_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteo',
            name='fecha',
            field=models.DateField(verbose_name='Fecha'),
        ),
    ]