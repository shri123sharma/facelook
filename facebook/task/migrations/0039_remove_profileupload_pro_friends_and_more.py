# Generated by Django 4.1 on 2022-09-12 12:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0038_merge_20220912_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileupload',
            name='pro_friends',
        ),
        migrations.AddField(
            model_name='profileupload',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='friends', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='friendlist',
            name='friend',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='friendlist',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userfriend', to=settings.AUTH_USER_MODEL),
        ),
    ]
