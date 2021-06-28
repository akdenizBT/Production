# Generated by Django 2.1.5 on 2021-05-10 16:05

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_author', models.CharField(max_length=50, verbose_name='İsim')),
                ('comment_content', models.CharField(max_length=256, verbose_name='Yorum')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-comment_date'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Başlık')),
                ('content', ckeditor.fields.RichTextField()),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('news_image', models.FileField(blank=True, null=True, upload_to='', verbose_name='Habere Fotoğraf Ekleyiniz.')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yazar')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='news.News', verbose_name='Haber'),
        ),
    ]