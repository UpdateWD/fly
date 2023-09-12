import sqlite3


def create_database():
    db_filename = 'my_database.db'
    try:
        conn = sqlite3.connect(db_filename)
        cursor = conn.cursor()
    except sqlite3.Error as e:
        print(f"Ошибка при подключении к базе данных: {e}")
        return

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS my_table (
        id INTEGER PRIMARY KEY,
        tg_id TEXT,
        id_key TEXT,
        accessurl TEXT,
        time TEXT,
        refferals TEXT,
        trial INTEGER
    );
    '''

    try:
        cursor.execute(create_table_query)
        conn.commit()
        print("Таблица успешно создана или уже существует.")
    except sqlite3.Error as e:
        print(f"Ошибка при создании таблицы: {e}")
    finally:
        conn.close()
