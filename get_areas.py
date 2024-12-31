import os
import requests
import csv
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение данных из переменных окружения
hh_user_access_token = os.getenv('HH_USER_ACCESS_TOKEN')
app_name = os.getenv('APP_NAME')
dev_email = os.getenv('DEV_EMAIL')

# URL для получения списка городов
url = "https://api.hh.ru/salary_statistics/dictionaries/salary_areas"

# Заголовки запроса
headers = {
    "Authorization": f"Bearer {hh_user_access_token}",
    "HH-User-Agent": f"{app_name} ({dev_email})"
}

# Параметры запроса
params = {
    "locale": "RU",
    "host": "hh.ru"
}

def fetch_areas():
    """
    Получение списка регионов, областей и городов с API.

    :return: Список областей с городами.
    """
    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch areas. Status code:", response.status_code)
            print("Response:", response.text)
            return None
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return None

def save_to_csv(data, filename="data/areas.csv"):
    """
    Сохранение данных в CSV файл.

    :param data: Данные для сохранения.
    :param filename: Имя файла для сохранения.
    """
    with open(filename, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        # Записываем заголовки
        writer.writerow(["Country", "Region", "City", "City ID"])
        
        def write_area(area, country_name=""):
            for region in area.get("areas", []):
                for city in region.get("areas", []):
                    writer.writerow([
                        country_name, region["name"], city["name"], city["id"]
                    ])

        # Рекурсивно записываем данные
        for country in data:
            write_area(country, country_name=country["name"])

# Получение данных
areas_data = fetch_areas()
if areas_data:
    save_to_csv(areas_data)
    print("Данные успешно сохранены в areas.csv")
else:
    print("Не удалось получить данные.")
