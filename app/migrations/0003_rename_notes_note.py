# Generated by Django 3.2.21 on 2023-09-28 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_notes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notes',
            new_name='Note',
        ),
    ]
