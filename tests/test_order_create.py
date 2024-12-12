import allure
import pytest
from methods.order_methods import OrderMethods
from conftest import temp_order


@allure.suite('Тесты на создание заказа')
class TestCreateOrder:
    @allure.title('Тест на создание заказа')
    @pytest.mark.parametrize('color',["GREY","BLACK", "",
                                      ["GREY", "BLACK"]])
    def test_order_create_color_parametrize_order_created(self, temp_order, color):
        response = OrderMethods.create_order_with_payload(temp_order, color)
        data = response.json()

        assert response.status_code == 201 and "track" in data
