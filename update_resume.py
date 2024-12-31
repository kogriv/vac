import os
import requests
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение данных из переменных окружения
hh_user_access_token = os.getenv('HH_USER_ACCESS_TOKEN')
app_name = os.getenv('APP_NAME')
dev_email = os.getenv('DEV_EMAIL')
resume_id = os.getenv('RESUME_ID')

# URL для обновления резюме
url = f"https://api.hh.ru/resumes/{resume_id}"

# Заголовки запроса
headers = {
    "Authorization": f"Bearer {hh_user_access_token}",
    "HH-User-Agent": f"{app_name} ({dev_email})",
    "Content-Type": "application/json"
}

# Путь к файлу с описанием навыков
skills_file_path = "data/skills.txt"

def read_skills_from_file(file_path):
    """
    Чтение текста с описанием навыков из файла.

    :param file_path: Путь к файлу.
    :return: Текст из файла или None, если файл не найден или пуст.
    """
    try:
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                skills = file.read().strip()
                return skills if skills else None
        else:
            return None
    except Exception as e:
        print("Ошибка при чтении файла с навыками:", e)
        return None

# Формирование тела запроса
skills = read_skills_from_file(skills_file_path) or "Perhaps the best data scientist in the south of Kuzbass"

# print(skills)

body = {
    # "birth_date": "1999-06-25", - baba yagodka opyat
    "skills": skills
}

def update_resume(body):
    """
    Обновление данных резюме.

    :param body: Тело запроса с данными.
    :return: Ответ сервера или None при ошибке.
    """
    try:
        # Выполнение PUT-запроса
        response = requests.put(url, headers=headers, json=body)

        # Проверка статуса ответа
        if response.status_code == 204:
            print("Резюме успешно обновлено.")
            return response
        else:
            print("Не удалось обновить резюме. Код ответа:", response.status_code)
            print("Ответ:", response.text)
            return response

    except requests.exceptions.RequestException as e:
        print("Произошла ошибка:", e)
        return None

# Тестирование функции
res = update_resume(body)
print(res)
