import requests
import json
import sqlite3

def create_key_and_update_db(user_id):
    api_url = 'https://194.67.67.219:29969/4HmD7UFS6UTu3Xn7xWeXiQ/access-keys'
    json_data = {"method": "aes-192-gcm"}

    headers = {
        "Content-Type": "application/json"  # Устанавливаем заголовок Content-Type
    }

    try:
        # Выполняем POST-запрос с заголовком application/json
        response = requests.post(api_url, json=json_data, headers=headers, verify=False)
        response.raise_for_status()  # Проверяем, что запрос прошел успешно

        # Получаем JSON-ответ
        json_response = response.json()

        # Извлекаем данные из JSON
        access_url = json_response.get("accessUrl")
        key_id = json_response.get("id")

        # Обновляем имя ключа с использованием user_id
        new_name = str(user_id)  # Используем user_id для имени ключа
        update_key_name(key_id, new_name)

        # Обновляем данные о лимите
        update_data_limit(key_id)

        # Подключение к базе данных
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()

        # Обновляем запись пользователя в базе данных с полученными данными
        cursor.execute("UPDATE my_table SET id_key=?, accessurl=? WHERE tg_id=?", (key_id, access_url, user_id))
        conn.commit()

        # Закрываем соединение с базой данных
        conn.close()

        return access_url, key_id
    except Exception as e:
        print(f"Error: {str(e)}")
        return None, None

def update_key_name(key_id, new_name):
    api_url = f'https://194.67.67.219:29969/4HmD7UFS6UTu3Xn7xWeXiQ/access-keys/{key_id}/name'
    json_data = {"name": new_name}

    headers = {
        "Content-Type": "application/json"  # Устанавливаем заголовок Content-Type
    }

    try:
        # Выполняем PUT-запрос с обновлением имени ключа
        response = requests.put(api_url, json=json_data, headers=headers, verify=False)
        response.raise_for_status()  # Проверяем, что запрос прошел успешно

        # Возвращаем результат запроса
        return response.json()
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def update_data_limit(key_id):
    api_url = f'https://194.67.67.219:29969/4HmD7UFS6UTu3Xn7xWeXiQ/access-keys/{key_id}/data-limit'
    json_data = {"limit": {"bytes": 100000000000}}

    headers = {
        "Content-Type": "application/json"  # Устанавливаем заголовок Content-Type
    }

    try:
        # Выполняем PUT-запрос с обновлением данных о лимите
        response = requests.put(api_url, json=json_data, headers=headers, verify=False)
        response.raise_for_status()  # Проверяем, что запрос прошел успешно

        # Возвращаем результат запроса
        return response.json()
    except Exception as e:
        print(f"Error: {str(e)}")
        return None
