# Generated by Django 2.2 on 2021-01-28 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('astudent', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentmodel',
            old_name='fisrt_name',
            new_name='first_name',
        ),
    ]
