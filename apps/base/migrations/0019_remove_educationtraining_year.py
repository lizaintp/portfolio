# Generated by Django 5.0.4 on 2024-04-27 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_alter_contacts_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='educationtraining',
            name='year',
        ),
    ]
