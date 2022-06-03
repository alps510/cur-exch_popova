import requests
import json
from config import keys, API_KEY


class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise APIException(f'Вы ввели одинаковые валюты {quote}')

        try:
            quote_base = keys[quote] + keys[base]
        except KeyError:
            raise APIException(f'Невозможно обработать валюту {quote}, {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Невозможно обработать количество {amount}')

        r = requests.get(f'https://currate.ru/api/?get=rates&pairs={quote_base}&key={API_KEY}')
        total_base = float(json.loads(r.content)['data'][quote_base]) * amount
        total_base = format(total_base, '.3f')
        return total_base
