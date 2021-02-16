# Generated by Django 3.1.5 on 2021-02-15 20:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandleSiteComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=1024)),
                ('rate', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('candlesite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.candlesite')),
            ],
        ),
    ]
