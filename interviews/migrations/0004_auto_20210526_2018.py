# Generated by Django 2.1.5 on 2021-05-26 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interviews', '0003_auto_20210526_1957'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interviews',
            old_name='favourite',
            new_name='favourite_interviews',
        ),
    ]
