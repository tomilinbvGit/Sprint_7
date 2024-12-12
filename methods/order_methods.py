import allure
import requests
from urls import URLS


class OrderMethods:
    @staticmethod
    @allure.step("Создание заказа с указанными параметрами")
    def create_order_with_payload(data, color):
        payload = data
        payload["color"] = color if isinstance(color,list) else [color]
        url = f'{URLS["BASE_URL"]}{URLS["ORDERS_URL"]}'
        response = requests.post(url, json=payload)

        return response


    @staticmethod
    @allure.step("Получение списка всех заказов")
    def get_order_list():
        url = f'{URLS["BASE_URL"]}{URLS["ORDERS_URL"]}'
        response = requests.get(url)

        return response
