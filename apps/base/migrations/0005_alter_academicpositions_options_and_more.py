# Generated by Django 5.0.4 on 2024-04-26 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_delete_settings_portfolio_subreview'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='academicpositions',
            options={'verbose_name': 'Академическая должность', 'verbose_name_plural': 'Академическии должности'},
        ),
        migrations.AlterModelOptions(
            name='educationtraining',
            options={'verbose_name': 'Образование/Обучение', 'verbose_name_plural': 'Образовании/Обучении'},
        ),
        migrations.AlterModelOptions(
            name='portfolio',
            options={'verbose_name': '1)Портфолио', 'verbose_name_plural': '1)Портфолии'},
        ),
    ]
