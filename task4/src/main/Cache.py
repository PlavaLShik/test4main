from abc import ABC, abstractmethod
from Api import ApilayerCurrencyConverter

#Абстрактный класс кэша
class AbstractCache(ABC):
    @abstractmethod
    def get_cached_exchange_rate(self, from_currency, to_currency, amount):
        pass
#Класс кэша для конкретного API
class ApilayerCache(AbstractCache):
    def __init__(self):
        self._cache = {}

    def get_cached_exchange_rate(self, from_currency, to_currency, amount):
        key = f"{from_currency}-{to_currency}-{amount}"
        if key in self._cache:
            return self._cache[key]
        else:
            api_call = ApilayerCurrencyConverter().get_current_exchange_rate(from_currency, to_currency, amount)
            self._cache[key] = api_call
            return api_call