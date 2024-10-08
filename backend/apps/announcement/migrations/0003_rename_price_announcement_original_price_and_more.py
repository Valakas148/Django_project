# Generated by Django 5.1 on 2024-09-03 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0002_announcement_place'),
    ]

    operations = [
        migrations.RenameField(
            model_name='announcement',
            old_name='price',
            new_name='original_price',
        ),
        migrations.AddField(
            model_name='announcement',
            name='exchange_rate_eur',
            field=models.DecimalField(decimal_places=4, default=5, help_text='EUR to UAH', max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='announcement',
            name='exchange_rate_usd',
            field=models.DecimalField(decimal_places=4, default=5, help_text='USD to UAH', max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='announcement',
            name='original_currency',
            field=models.CharField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('UAH', 'UAH')], default=5, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='announcement',
            name='price_eur',
            field=models.DecimalField(decimal_places=2, default=5, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='announcement',
            name='price_uah',
            field=models.DecimalField(decimal_places=2, default=5, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='announcement',
            name='price_usd',
            field=models.DecimalField(decimal_places=2, default=5, max_digits=10),
            preserve_default=False,
        ),
    ]
