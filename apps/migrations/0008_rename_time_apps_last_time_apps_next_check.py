# Generated by Django 4.0 on 2021-12-13 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0007_apps_start_time_alter_folders_name_folder'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apps',
            old_name='time',
            new_name='last_time',
        ),
        migrations.AddField(
            model_name='apps',
            name='next_check',
            field=models.CharField(default='None', max_length=50, verbose_name='Следующее обновление'),
        ),
    ]