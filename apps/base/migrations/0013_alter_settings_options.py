# Generated by Django 5.0.4 on 2024-04-26 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_remove_settings_adout'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name': 'Основная настройка', 'verbose_name_plural': 'Основные настройки'},
        ),
    ]
