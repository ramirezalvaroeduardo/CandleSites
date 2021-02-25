# Generated by Django 3.1.5 on 2021-02-25 04:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0007_auto_20210224_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candlesitecomments',
            name='commentator',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
