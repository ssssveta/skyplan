import sqlite3

def weather_data_write():
    '''
    Функция получает ... и записывает данные по городу в таблицу WeatherData
    '''
    pass

def users_profilies_write(username, email, password):
    conn = sqlite3.connect('WeatherDB.db')
    cursor = conn.cursor()
    try:
        cursor.execute("""INSERT INTO UsersProfiles (username, email, password) VALUES (?, ?, ?)""", (username, email, password))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Пользователь с ником {username} или почтой {email} уже существует")
    conn.close()

def users_requests_write(request_id, user_id, request_city_id, recommendation_id):
    '''
    Функция получает ... и записывает данные в таблицу UsersRequests
    '''
    pass

def users_recommendation_write(recommendation):
    '''
    Функция записывает recommendation в таблицу UsersRecommendation
    '''
    conn = sqlite3.connect('WeatherDB.db', isolation_level=None)
    cursor = conn.cursor()
    try:
        cursor.execute("""INSERT INTO UsersRecommendation (recommendation) VALUES (?)""", (recommendation))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Рекомендация  {recommendation} уже существует в таблице UsersRecommendation")

