# Generated by Django 2.1.5 on 2021-06-12 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20210612_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='read',
            field=models.IntegerField(default=0),
        ),
    ]