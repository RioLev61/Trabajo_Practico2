# Generated by Django 3.2.14 on 2022-12-04 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cac', '0003_auto_20221124_2345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posteo',
            name='usuario',
        ),
    ]