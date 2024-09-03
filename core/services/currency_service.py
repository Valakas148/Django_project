from decimal import Decimal

import requests


def get_exchange_rates():
    response = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
    data = response.json()
    rates = {item['ccy']: item['sale'] for item in data}
    return rates


def update_prices(announcement):
    rates = get_exchange_rates()
    original_price = Decimal(announcement.original_price)
    if announcement.original_currency == 'USD':
        announcement.price_uah = original_price * Decimal(rates['USD'])
        announcement.price_eur = (original_price * Decimal(rates['USD'])) / Decimal(rates['EUR'])
    elif announcement.original_currency == 'EUR':
        announcement.price_uah = original_price * Decimal(rates['EUR'])
        announcement.price_usd = (original_price * Decimal(rates['EUR'])) / Decimal(rates['USD'])
    elif announcement.original_currency == 'UAH':
        announcement.price_usd = original_price / Decimal(rates['USD'])
        announcement.price_eur = original_price / Decimal(rates['EUR'])
        announcement.price_uah = original_price
    else:
        raise ValueError("Unsupported currency type.")

    announcement.exchange_rate_usd = Decimal(rates['USD'])
    announcement.exchange_rate_eur = Decimal(rates['EUR'])
    announcement.save()

