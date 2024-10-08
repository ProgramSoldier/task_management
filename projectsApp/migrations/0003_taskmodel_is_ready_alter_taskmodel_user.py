# Generated by Django 5.0.3 on 2024-08-08 08:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectsApp', '0002_remove_projectmodel_author_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='is_ready',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
