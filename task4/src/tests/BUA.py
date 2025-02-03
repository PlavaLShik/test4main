import requests
import pytest


@pytest.mark.parametrize("url,username,password,new_password", [
    ("https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from}&amount={amount}", "user",
     "correct_password", "new_password")
])
def test_broken_user_authentication(url, username, password, new_password):
    """
    Тест на Broken User Authentication
    """
    # Аутентифицируемся как пользователь
    response = requests.post("https://api.apilayer.com/login", json={"username": username, "password": password,
                                                                     "api_key": "SmeaAphpSsdDQYGzZDXK1lZzqUEbVocQ"})
    assert response.status_code == 200

    # Попытка изменить пароль без выхода из сессии
    response = requests.post(url, json={"old_password": password, "new_password": "qwerty123"})

    # Проверка статуса ответа
    assert response.status_code == 403, f"Unexpected response code: {response.status_code}"
    assert response.text.startswith("Forbidden"), f"Unexpected response content: {response.text}"

