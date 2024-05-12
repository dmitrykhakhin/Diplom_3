import string
import random
import requests

from data import Url


class Helper:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def generate_random_email():
        random_email = Helper.generate_random_string(10) + 'yandex.ru'
        return random_email

    @staticmethod
    def generate_registration_data():
        email = Helper.generate_random_string(10) + '@yandex.ru'
        password = Helper.generate_random_string(10)
        name = Helper.generate_random_string(10)

        registration_data = {
            "email": email,
            "password": password,
            "name": name
        }
        return registration_data


class User:
    @staticmethod
    def register_new_user_and_return_response(payload):
        response = requests.post(Url.URL + Url.REGISTER_USER_HANDLE, data=payload)
        return response

    @staticmethod
    def delete_user(token, email):
        requests.delete(Url.URL + Url.AUTHORIZATION_USER_HANDLE,
                        headers={'Authorization': token},
                        data={"email": email})


class Order:
    @staticmethod
    def create_order_with_auth_and_return_response(token, ingredient_list):
        response = requests.post(Url.URL + Url.ORDERS_HANDLE,
                                 headers={'Authorization': token},
                                 data={"ingredients": ingredient_list})
        return response.json()
