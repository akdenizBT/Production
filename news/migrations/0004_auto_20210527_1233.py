# Generated by Django 2.1.5 on 2021-05-27 09:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0003_remove_news_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='favourite_news',
            field=models.ManyToManyField(blank=True, related_name='favourite_news', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='news',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes_news', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='news',
            name='read',
            field=models.IntegerField(default=0),
        ),
    ]
