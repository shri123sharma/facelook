# Generated by Django 4.1 on 2022-08-26 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0011_remove_post_dis_likes_remove_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagepost',
            name='messagefriend',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messagefriend', to='task.friend'),
        ),
    ]
