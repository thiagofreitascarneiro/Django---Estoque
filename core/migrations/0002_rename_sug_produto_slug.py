# Generated by Django 3.2.6 on 2021-08-23 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='sug',
            new_name='slug',
        ),
    ]
