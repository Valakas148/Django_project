# Generated by Django 5.1 on 2024-09-03 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0004_alter_announcement_price_eur_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='exchange_rate_eur',
            field=models.DecimalField(blank=True, decimal_places=4, help_text='EUR to UAH', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='exchange_rate_usd',
            field=models.DecimalField(blank=True, decimal_places=4, help_text='USD to UAH', max_digits=10, null=True),
        ),
    ]
