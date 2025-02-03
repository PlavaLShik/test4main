from Api import ApilayerCurrencyConverter
from Cache import ApilayerCache



#Класс клиента
class CurrencyClient:
    def __init__(self):
        self._api_caller = ApilayerCurrencyConverter()
        self._cache = ApilayerCache()

    def get_exchange_rate(self, from_currency, to_currency, amount):
        rate = self._cache.get_cached_exchange_rate(from_currency, to_currency, amount)
        if not rate:
            rate = self._api_caller.get_current_exchange_rate(from_currency, to_currency, amount)
            self._cache.get_cached_exchange_rate(from_currency, to_currency, amount)
        return rate

client = CurrencyClient()
rate = client.get_exchange_rate("USD", "EUR", "100")
print(rate)