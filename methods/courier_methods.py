import allure
from urls import URLS
import requests


class CourierMethods:
    @staticmethod
    @allure.step("Регистрация нового курьера")
    def register_new_courier_with_payload(payload):
        url = f'{URLS['BASE_URL']}{URLS['COURIER_URL']}'
        response = requests.post(url, json=payload)

        return response

    @staticmethod
    @allure.step("Создание УЗ курьера и его последующая авторизация")
    def courier_create_and_login_with_payload(payload):
        url = f'{URLS['BASE_URL']}{URLS['COURIER_URL']}'
        requests.post(url, json=payload)
        url = f'{URLS['BASE_URL']}{URLS['COURIER_LOGIN_URL']}'
        response = requests.post(url, json=payload)

        return response

    @staticmethod
    @allure.step("Авторизация курьера по логину и паролю")
    def courier_login(payload):
        url = f'{URLS['BASE_URL']}{URLS['COURIER_LOGIN_URL']}'
        response = requests.post(url, json=payload)

        return response
