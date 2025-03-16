import sqlite3

db=sqlite3.connect('WeatherDB.db')
cursor = db.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS City   
                (city_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name_city TEXT  NOT NULL,
                lat REAL,
                lng REAL) """)

cursor.execute("""CREATE TABLE IF NOT EXISTS UsersProfiles (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL) """)

cursor.execute("""CREATE TABLE IF NOT EXISTS UsersRequests (
            request_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            request_city_id INTEGER,
            recommendation_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES UsersProfiles(user_id),
            FOREIGN KEY (request_city_id) REFERENCES City(city_id),
            FOREIGN KEY (recommendation_id) REFERENCES UsersRecommendation(recommendation_id)) """)

cursor.execute("""CREATE TABLE IF NOT EXISTS UsersRecommendation (
                recommendation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                recommendation TEXT NOT NULL UNIQUE) """)

cursor.execute("""CREATE TABLE IF NOT EXISTS WeatherData (
            weather_id INTEGER PRIMARY KEY AUTOINCREMENT,
            city_id INTEGER,
            time DATETIME,
            tavg REAL,
            tmin REAL,
            tmax REAL,
            prcp REAL,
            snow REAL,
            wdir REAL,
            wspd REAL,
            wpgt REAL,
            pres REAL,
            tsun REAL,
            FOREIGN KEY (city_id) REFERENCES City(city_id)) """)
db.commit()
cursor.close()
db.close()
