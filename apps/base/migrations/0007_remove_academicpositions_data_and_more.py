# Generated by Django 5.0.4 on 2024-04-26 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_academicpositions_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academicpositions',
            name='data',
        ),
        migrations.RemoveField(
            model_name='academicpositions',
            name='place',
        ),
        migrations.AddField(
            model_name='academicpositions',
            name='place_data',
            field=models.CharField(default=1, max_length=255, verbose_name='Учебное заведение и дата'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='academicpositions',
            name='title',
            field=models.CharField(default=1, max_length=255, verbose_name='Название тайтла'),
            preserve_default=False,
        ),
    ]
