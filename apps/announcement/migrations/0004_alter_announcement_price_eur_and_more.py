# Generated by Django 5.1 on 2024-09-03 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0003_rename_price_announcement_original_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='price_eur',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='price_uah',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='price_usd',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
