import sqlite3
import pandas as pd
from meteostat import Point, Daily
from datetime import datetime, timedelta

conn = sqlite3.connect('WeatherDB.db')
cursor = conn.cursor()

csv_file = 'C:/Users/User/Desktop/skyplan/данные по городам(Россия)/ru.csv'
cities_df = pd.read_csv(csv_file)
for index, row in cities_df.iterrows():
    city_name=row["city"]
    lat=row["lat"]
    lng=row["lng"]
    cursor.execute("INSERT INTO City (name_city, lat, lng) VALUES (?, ?, ?)", (city_name, lat, lng))
conn.commit()

cursor.execute("SELECT city_id, name_city, lat, lng FROM City")
cities = cursor.fetchall()


for city_id, city_name, lat, lng in cities:
    #объект Point для города
    point = Point(lat, lng)
   
    #данные за 2005-2025 по России
    end = datetime.now()
    start = datetime.now()-timedelta(days=365*20)


    data = Daily(point, start, end)
    weather_data = data.fetch()

    for date, row in weather_data.iterrows():
        cursor.execute("""
            INSERT INTO WeatherData (city_id, time, tavg, tmin, tmax, prcp, snow, wdir, wspd, wpgt, pres, tsun)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (city_id, date.to_pydatetime(), row['tavg'], row['tmin'], row['tmax'], row['prcp'], row['snow'],
              row['wdir'], row['wspd'], row['wpgt'], row['pres'], row['tsun']))

    conn.commit()

'''

query = "SELECT name FROM sqlite_master WHERE type='table';"
cursor.execute(query)
tables = cursor.fetchall()

query = """SELECT * FROM City"""
cursor.execute(query)
rows = cursor.fetchall()
column_names = [description[0] for description in cursor.description]
print("\t".join(column_names))
for row in rows:
    print("\t".join(map(str, row)))
'''

print("Данные загружены")
