import requests
import json
from convention import keys

class ConvertException(Exception):
    pass

class WalletConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertException('невозможный перевод')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertException
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertException
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertException

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]
        return total_base * amount