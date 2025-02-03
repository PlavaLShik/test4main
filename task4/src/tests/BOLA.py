import requests
import pytest


@pytest.mark.parametrize("url,username,password,expected_response", [
    ("https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from1}&amount={amount}", "user",
     "correct_password", "Forbidden"),
    ("https://api.apilayer.com/admin_resource", "admin", "correct_password", "Forbidden")
])
def test_broken_object_level_authorization(url, username, password, expected_response):
    """
    Тест на Broken Object Level Authorization
    """
    # Аутентифицируемся как пользователь
    response = requests.post("https://api.apilayer.com/login", json={"username": username, "password": password,
                                                                     "api_key": "SmeaAphpSsdDQYGzZDXK1lZzqUEbVocQ"})
    assert response.status_code == 200

    # Попытка доступа к защищенному ресурсу
    response = requests.get(url.format(to="USD", from1="EUR", amount = "100"))

    # Проверка статуса ответа
    assert response.status_code == expected_response.status_code, f"Unexpected response code: {response.status_code}"
    assert response.text.startswith(expected_response.text), f"Unexpected response content: {response.text}"