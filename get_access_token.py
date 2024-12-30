import requests
from dotenv import load_dotenv
import os

load_dotenv()
hh_app_id  = os.getenv('HH_ID')
hh_app_secret = os.getenv('HH_SECRET')

# URL для получения токена
url = "https://api.hh.ru/token"

# Данные для запроса
data = {
    "grant_type": "client_credentials",
    "client_id": hh_app_id,
    "client_secret": hh_app_secret
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
    else:
        print("Failed to retrieve token. Status code:", response.status_code)
        print("Response:", response.text)

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)

