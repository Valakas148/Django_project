# Generated by Django 5.1 on 2024-09-04 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0006_announcement_view_count_announcement_views_last_day_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='edit_attempts',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
