import allure
import pytest
from helpers import generate_random_courier
from methods.courier_methods import CourierMethods
from conftest import temp_courier
from data import RESULTS


@allure.suite("Тесты на логин курьера в системе")
class TestCourierLogin:
    @allure.title("Успешная авторизация с валидными данными")
    def test_courier_login_with_valid_data_login_succeeded(self, temp_courier):
        response = CourierMethods.courier_create_and_login_with_payload(temp_courier)
        data = response.json()
        assert response.status_code == 200 and data['id'] != 0

    @allure.title("Авторизация курьера с отсутствующим обязательным полем")
    @pytest.mark.parametrize('missing_field', ['login','password'])
    def test_courier_login_with_missing_field_shows_error(self, missing_field):
        payload = generate_random_courier()
        # Через параметризацию заменяем значение для элемента на пустую строку
        payload[missing_field] = ""
        response = CourierMethods.courier_create_and_login_with_payload(payload)

        assert response.status_code == 400 and response.json() == RESULTS['MISSING_LOGIN_DATA']

    @allure.title("Авторизация курьера с несуществующей УЗ")
    def test_courier_login_with_no_such_login_shows_error(self):
        payload = generate_random_courier()
        response = CourierMethods.courier_login(payload)

        assert response.status_code == 404 and response.json() == RESULTS['NO_SUCH_LOGIN']
