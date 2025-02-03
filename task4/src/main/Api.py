from abc import ABC, abstractmethod
import requests

class AbstractApiCaller(ABC):
    @abstractmethod
    def get_current_exchange_rate(self, from_currency, to_currency, amount):
        pass

class ApilayerCurrencyConverter(AbstractApiCaller):
    BASE_URL = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from1}&amount={amount}"
    API_KEY = "SmeaAphpSsdDQYGzZDXK1lZzqUEbVocQ"

    def get_current_exchange_rate(self, from_currency, to_currency, amount):
        url = self.BASE_URL.format(to=to_currency, from1=from_currency, amount=amount)
        headers = {"X-Api-Key": self.API_KEY}
        response = requests.get(url, headers=headers)
        return response.text

# Пример использования класса
converter = ApilayerCurrencyConverter()
from_currency = "USD"
to_currency = "EUR"
amount = "100"
result = converter.get_current_exchange_rate(from_currency, to_currency, amount)
print(result)