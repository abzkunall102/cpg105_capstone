# Generated by Django 3.2.9 on 2021-11-05 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ml', '0002_mlmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='fname',
            new_name='name',
        ),
    ]
