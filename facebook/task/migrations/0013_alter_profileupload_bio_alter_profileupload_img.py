# Generated by Django 4.1 on 2022-08-26 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0012_messagepost_messagefriend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileupload',
            name='bio',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='profileupload',
            name='img',
            field=models.ImageField(default='', upload_to='profile_image'),
        ),
    ]
