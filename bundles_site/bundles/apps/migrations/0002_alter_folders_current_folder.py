# Generated by Django 4.0 on 2021-12-10 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folders',
            name='current_folder',
            field=models.BooleanField(default=False, verbose_name='Текущая папка'),
        ),
    ]