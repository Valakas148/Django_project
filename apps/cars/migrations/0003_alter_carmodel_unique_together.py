# Generated by Django 5.1 on 2024-09-05 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_carmodel_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='carmodel',
            unique_together=set(),
        ),
    ]
