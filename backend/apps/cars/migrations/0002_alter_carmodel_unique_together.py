# Generated by Django 5.1 on 2024-09-05 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='carmodel',
            unique_together={('brand', 'model', 'year', 'body_type')},
        ),
    ]
