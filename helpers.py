import string
import random
from faker import Faker


def generate_random_string(): # Генератор строки
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(15))
    return random_string


def generate_random_courier(): # Генератор словаря с данными для курьера
    login, password, first_name = (generate_random_string() for _ in range(3))
    full_courier_info = {
        'login': login,
        'password': password,
        'first_name': first_name
    }
    return full_courier_info

def generate_order_data(): # Генератор словаря с данными для тестирования заказа
    faker = Faker("ru_RU")
    payload = {
        "firstName": faker.first_name(),
        "lastName": faker.last_name(),
        "address": faker.address(),
        "metroStation": faker.random_int(1, 20),
        "phone": faker.phone_number(),
        "rentTime": faker.random_int(1, 7),
        "deliveryDate": faker.future_date().strftime("%Y-%m-%d"),
        "comment": faker.sentence(),
        "color": None # Цвет задается через параметризацию в тестах
    }

    return payload
