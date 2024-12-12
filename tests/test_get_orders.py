import allure
from methods.order_methods import OrderMethods


@allure.suite("Получение полного списка заказов")
class TestGetFullOrderList:
    @allure.title("Успешное получение полного списка заказов")
    def test_get_all_orders_list__of_orders_received(self):
        response = OrderMethods.get_order_list()
        data = response.json()

        assert response.status_code == 200 and data["orders"] != []
