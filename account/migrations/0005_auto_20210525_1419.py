# Generated by Django 2.1.5 on 2021-05-25 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20210525_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_avatar',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Fotoğraf ekle'),
        ),
    ]