# Generated by Django 4.1 on 2022-08-23 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_remove_post_post_title_post_post_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_type',
        ),
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='post_images'),
        ),
    ]
