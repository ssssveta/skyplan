from meteostat import Point, Daily
from datetime import datetime, timedelta
from sqlalchemy import create_engine
import sqlite3
#локация - Москва
latitude=55.7558
longitude=37.6173
location=Point(latitude,longitude)

#данные: за последние 30 лет
end_date=datetime.now()
start_date=end_date-timedelta(days=365*20)

data=Daily(location,start=start_date,end=end_date)
data=data.fetch()
print(data.head())
data_size=data.shape
print(f"Размер данных: {data_size}")
#данные нужно обработать..

#создание локальной БД - SQLite
print('test SQL db')
engine = create_engine('sqlite:///weather_data.db')
data.to_sql('weather', con=engine, if_exists='replace', index=True)

connect = sqlite3.connect('weather_data.db')
#cursor = conn.cursor()
#cursor.execute("SELECT * FROM weather")
#rows = cursor.fetchall()
#for row in rows:
#        print(row)
#сonn.close()
