import os
import requests
from urllib.parse import urlencode
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение данных из переменных окружения
hh_app_id = os.getenv('HH_ID')
# print(hh_app_id)
hh_app_secret = os.getenv('HH_SECRET')
# print(hh_app_secret)
redirect_uri = os.getenv('HH_REDIRECT_URI')
# print(redirect_uri)



# Проверка, что все переменные окружения заданы
if not hh_app_id or not hh_app_secret or not redirect_uri:
    print("Ошибка: убедитесь, что HH_APP_ID, HH_SECRET и HH_REDIRECT_URI указаны в .env.")
    exit(1)

# URL для получения токена
url = "https://hh.ru/oauth/token"

def get_access_token(auth_code):
    """
    Получение access_token для пользователя.

    :param auth_code: authorization_code, полученный после редиректа.
    :return: словарь с данными токена или None при ошибке.
    """
    # Данные для запроса
    data = {
        "grant_type": "authorization_code",
        "client_id": hh_app_id,
        "client_secret": hh_app_secret,
        "redirect_uri": redirect_uri,
        "code": auth_code
    }

    # Заголовки запроса
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    try:
        # Выполнение POST-запроса
        response = requests.post(url, data=data, headers=headers)

        # Проверка статуса ответа
        if response.status_code == 200:
            token_info = response.json()
            print("Access Token:", token_info["access_token"])
            return token_info
        else:
            print("Failed to retrieve token. Status code:", response.status_code)
            print("Response:", response.json())
            return None

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return None

state = "optional_custom_state"  # Необязательный параметр для отслеживания сессии

# Базовый URL для авторизации
base_url = "https://hh.ru/oauth/authorize"

# Формирование параметров
params = {
    "response_type": "code",
    "client_id": hh_app_id,
    "redirect_uri": redirect_uri,
    "state": state,
}

# Создание полной ссылки
auth_url = f"{base_url}?{urlencode(params)}"

print("Перейдите по следующей ссылке для авторизации:")
print(auth_url)

# Получение authorization_code от пользователя
auth_code = input("Введите полученный authorization_code из URL (параметр code): ")

# Получение access_token
get_access_token(auth_code)
