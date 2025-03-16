import sqlite3

def weather_data_get(name_city):
    '''
    Функция получает название города и возвращает по городу данные из таблицы WeatherData
    '''

    conn = sqlite3.connect('WeatherDB.db')
    cursor = conn.cursor()
    cursor.execute("SELECT city_id FROM City WHERE name_city = ?", (name_city,))
    city_id=cursor.fetchone()
    if city_id:
        cursor.execute("""SELECT * FROM WeatherData WHERE city_id = ?""", (city_id[0],))
        weather_data = cursor.fetchall()
        print(weather_data)
        return weather_data
    else:
        print(f'Город {city_name} не найден')

    conn.close()

def users_requests_get():
    '''
    Функция получает ... и возвращает  данные из таблицы UsersRequests
    '''
    pass

def users_recommendation_get():
    '''
    Функция получает ... и возвращает  данные из таблицы UsersRecommendation
    '''
    pass

