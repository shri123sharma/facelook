# Generated by Django 4.1 on 2022-09-05 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0021_remove_post_feeling_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='post_image'),
        ),
    ]
