# Generated by Django 4.0.6 on 2022-08-23 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_remove_post_post_name_remove_post_post_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='postlikes',
            name='like_status',
            field=models.BooleanField(default=False),
        ),
    ]
