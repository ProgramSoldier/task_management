# Generated by Django 5.0.3 on 2024-08-19 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectsApp', '0003_taskmodel_is_ready_alter_taskmodel_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temporary_links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
