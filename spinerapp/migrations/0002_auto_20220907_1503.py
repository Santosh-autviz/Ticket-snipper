# Generated by Django 3.2.13 on 2022-09-07 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spinerapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='Address1',
            new_name='Address',
        ),
        migrations.RemoveField(
            model_name='account',
            name='Address2',
        ),
    ]
