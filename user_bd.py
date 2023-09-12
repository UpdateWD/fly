import sqlite3

def create_user_if_not_exists(tg_id):
    # Подключение к базе данных
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    # Проверка наличия записи с tg_id в базе данных
    cursor.execute("SELECT tg_id FROM my_table WHERE tg_id=?", (tg_id,))
    existing_user = cursor.fetchone()

    if not existing_user:
        # Если записи нет, создаем новую
        cursor.execute("INSERT INTO my_table (tg_id, id_key, accessurl, time, refferals, trial) VALUES (?, ?, ?, ?, ?, ?)",
                       (tg_id, '', '', '', '', 0))
        conn.commit()

    # Закрываем соединение с базой данных
    conn.close()
