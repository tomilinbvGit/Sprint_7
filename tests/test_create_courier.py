import allure
import pytest
from helpers import generate_random_courier
from methods.courier_methods import CourierMethods
from conftest import temp_courier
from data import RESULTS


@allure.suite("Тесты на создание курьера в системе")
class TestCreateCourier:
    @allure.title("Успешное создание нового курьера")
    def test_create_courier_courier_created(self, temp_courier):
        response = CourierMethods.register_new_courier_with_payload(temp_courier)

        assert response.status_code == 201 and response.json() == RESULTS['SUCCEEDED_CREATE']

    @allure.title("Попытка создать дубликат курьера")
    def test_prevent_duplicate_courier_shows_error(self, temp_courier):
        # Отправляем первый запрос на создание курьера
        CourierMethods.register_new_courier_with_payload(temp_courier)
        # Отправляем второй запрос на создание курьера
        response = CourierMethods.register_new_courier_with_payload(temp_courier)

        assert response.status_code == 409 and response.json() == RESULTS['COURIER_CREATED_BEFORE']

    @allure.title("Создание курьера с отсутствующим обязательным полем")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_with_missing_field_shows_error(self, missing_field):
        payload = generate_random_courier()
        # Через параметризацию заменяем значение для элемента на пустую строку
        payload[missing_field] = ""
        response = CourierMethods.register_new_courier_with_payload(payload)

        assert response.status_code == 400 and response.json() == RESULTS['MISSING_CREATE']
