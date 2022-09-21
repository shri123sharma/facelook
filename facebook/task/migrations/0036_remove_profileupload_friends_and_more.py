# Generated by Django 4.1 on 2022-09-11 18:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0035_alter_friendlist_friend_alter_friendlist_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileupload',
            name='friends',
        ),
        migrations.AddField(
            model_name='profileupload',
            name='pro_friends',
            field=models.ManyToManyField(blank=True, null=True, related_name='pro_friends', to=settings.AUTH_USER_MODEL),
        ),
    ]
