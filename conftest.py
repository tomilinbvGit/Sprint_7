import pytest
import requests
from urls import URLS
from helpers import generate_order_data, generate_random_courier


@pytest.fixture()
def temp_courier():
    # Генерируем полный набор данных для курьера и передаем их в тест
    full_courier_info = generate_random_courier()
    print(full_courier_info)
    yield full_courier_info
    """После выполнения теста выполняем логин курьера (передаем логин и пароль), 
    получаем id и по нему выполняем удаление созданного курьера"""
    courier_login_info = {
        'login': full_courier_info["login"],
        'password': full_courier_info["password"]
    }
    response = requests.post(f'{URLS['BASE_URL']}{URLS['COURIER_LOGIN_URL']}', json=courier_login_info)
    courier_id = response.json()['id']
    if courier_id is not None:
        requests.delete(f'{URLS['BASE_URL']}{URLS['COURIER_URL']}{courier_id}')


# Фикстура создает при помощи генератора новый набор данных для заказа и передает их в тест
@pytest.fixture()
def temp_order():
    order_data = generate_order_data()
    return order_data
