# Generated by Django 4.1 on 2022-09-11 18:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0034_friendlist_updated_alter_friendlist_status'),
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
        migrations.AlterField(
            model_name='friendlist',
            name='friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='task.profileupload'),
        ),
        migrations.AlterField(
            model_name='friendlist',
            name='status',
            field=models.CharField(choices=[('send', 'send'), ('accepted', 'accepted')], max_length=8),
        ),
        migrations.AlterField(
            model_name='friendlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userfriend', to='task.profileupload'),
        ),
    ]
