# Generated by Django 2.1.5 on 2021-05-27 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20210525_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_avatar',
            field=models.FileField(blank=True, default='settings.MEDIA_ROOT/akdenız_logo.png', null=True, upload_to='', verbose_name='Fotoğraf ekle'),
        ),
    ]
