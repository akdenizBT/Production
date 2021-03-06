# Generated by Django 2.1.5 on 2021-05-21 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='journals',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='journals.Journals', verbose_name='Dergi'),
        ),
        migrations.AlterField(
            model_name='journals',
            name='journals_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Dergiye Kapak Fotoğraf Ekleyiniz.'),
        ),
    ]
