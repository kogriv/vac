import requests
import psycopg2
import schedule
import random
import time
import logging
from dotenv import load_dotenv
import os
from dbpro import *

load_dotenv()
hh_api_token = os.getenv('HH_APP_ACCESS_TOKEN')

vacancies = [
        'BI Developer', 'Business Development Manager', 'Community Manager', 'Computer vision',
        'Data Analyst', 'Data Engineer', 'Data Science', 'Data Scientist', 'ML Engineer',
        'Machine Learning Engineer', 'ML OPS инженер', 'ML-разработчик', 'Machine Learning',
        'Product Manager', 'Python Developer', 'Web Analyst', 'Аналитик данных',
        'Бизнес-аналитик', 'Веб-аналитик', 'Системный аналитик', 'Финансовый аналитик'
    ]

cities = {
        'Москва': 1,
        'Санкт-Петербург': 2
    }

vacs = get_vacancies(1,'Data Scientist',0,hh_api_token)

print(vacs)