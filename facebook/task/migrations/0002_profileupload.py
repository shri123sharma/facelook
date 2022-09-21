# Generated by Django 4.1 on 2022-08-21 07:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='profile_image')),
                ('profileuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profileuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
