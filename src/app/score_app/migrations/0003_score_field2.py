# Generated by Django 4.2 on 2023-04-15 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('score_app', '0002_remove_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='field2',
            field=models.TextField(default=''),
        ),
    ]
