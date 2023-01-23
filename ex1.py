import sqlite3 as sq

# #https://youtu.be/inHiIdZBIEc?list=PLA0M1Bcd0w8x4Inr5oYttMK6J47vxgv6J&t=133
# cars = [
#     ('Audi', 52642),
#     ('Mersedes', 57127),
#     ('Skoda', 9000),
#     ('Volvo', 29000),
#     ('Bentley', 350000)
# ]

# #Соединение с БД
# #https://www.youtube.com/watch?v=TCdyfEvrIUg&list=PLA0M1Bcd0w8x4Inr5oYttMK6J47vxgv6J&index=2
# with sq.connect('saper.db') as con: #https://youtu.be/inHiIdZBIEc?list=PLA0M1Bcd0w8x4Inr5oYttMK6J47vxgv6J&t=17
#     cur = con.cursor()

#     cur.execute("DROP TABLE IF EXISTS users")
#     cur.execute(""" CREATE TABLE IF NOT EXISTS users (
#         user_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         sex INTEGER NOT NULL DEFAULT 1,
#         old INTEGER,
#         score INTEGER
#         )""")
# #про sex INTEGER NOT NULL DEFAULT 1 https://youtu.be/fYGfBpuFu0A?list=PLA0M1Bcd0w8x4Inr5oYttMK6J47vxgv6J&t=121

#     cur.execute("""INSERT INTO users (name, sex, old, score)
#     VALUES 
#     ('Михаил', 1, 19, 1000),
#     ('Федор', 1, 32, 200),
#     ('Николай', 1, 22, 500),
#     ('Мария', 2, 18, 400),
#     ('Сергей', 1, 33, 2000),
#     ('Владимир', 1, 43, 100),
#     ('Елена', 2, 17, 500),
#     ('Юля', 2, 23, 700)""")

#     cur.execute('SELECT name, old, score FROM users WHERE score >= 700 ORDER BY name desc')
    
#     #Для получения результатов SELECT'а списком
#     result = cur.fetchall()
#     print(result)
        
#     #Для получения результатов SELECT'а типа как таблица, такой подход существенно экономит память(если данных много), т.к. не сохраняет список
#     for result in cur:
#         print (result)

#     result = cur.fetchone() #возвращает только 1ю запись
#     print(result)
#     result2 = cur.fetchmany(3) #возвращает указанное кол-во записей
#     print(result2)

# #Добавление записей в таблицу Python'ом
# #https://youtu.be/inHiIdZBIEc?list=PLA0M1Bcd0w8x4Inr5oYttMK6J47vxgv6J&t=133


#     cur.execute(""" CREATE TABLE IF NOT EXISTS cars (
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT NOT NULL,
#         price INTEGER NOT NULL
#     )""")

#     for car in cars:
#         cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)
    
#     #Аналогичный по функционалю циклу выше метод:
#     cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)

# #Добавление записей по именованым параметрам
# #https://youtu.be/inHiIdZBIEc?list=PLA0M1Bcd0w8x4Inr5oYttMK6J47vxgv6J&t=235
#     cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'A%'", {'Price': 0})

# #Выполнение нескольких SQL-команд в одном скрипте. ВНИМАНИЕ! Есть ограничение на использование SQL-запросов
# #записывает данные так как они есть
# #https://youtu.be/inHiIdZBIEc?list=PLA0M1Bcd0w8x4Inr5oYttMK6J47vxgv6J&t=293
#     cur.executescript("""DELETE FROM cars WHERE model LIKE 'A%';
#         UPDATE cars SET price = price + 1000
#     """)


# #Соединение с БД через блок обработки исключений - более лучший способ!!!
# #https://youtu.be/inHiIdZBIEc?list=PLA0M1Bcd0w8x4Inr5oYttMK6J47vxgv6J&t=349
# con = None
# try:
#     con = sq.connect('saper.db')
#     cur = con.cursor()

#     cur.executescript(""" CREATE TABLE IF NOT EXISTS cars (
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT NOT NULL,
#         price INTEGER NOT NULL
#         );
#         BEGIN;
#         INSERT INTO cars VALUES(NULL, 'Audi', 52642);
#         INSERT INTO cars VALUES(NULL, 'Mersedes', 57127);
#         INSERT INTO cars VALUES(NULL, 'Skoda', 9000);
#         INSERT INTO cars VALUES(NULL, 'Volvo', 29000);
#         INSERT INTO cars VALUES(NULL, 'Bentley', 350000);
#         UPDATE cars SET price = price + 1000
#     """)

#     con.commit()

# except sq.Error as e:
#     if con: con.rollback()
#     print("Ошибка выполнения запроса")
# finally:
#     if con: con.close()

# #Примерение свойства последней записи ID по .lastrowid
# #https://youtu.be/inHiIdZBIEc?list=PLA0M1Bcd0w8x4Inr5oYttMK6J47vxgv6J&t=588
# with sq.connect('saper.db') as con: #https://youtu.be/inHiIdZBIEc?list=PLA0M1Bcd0w8x4Inr5oYttMK6J47vxgv6J&t=17
#     con.row_factory = sq.Row # Для вывод данных в виде словаря: https://youtu.be/Ic6etzJZF-M?list=PLA0M1Bcd0w8x4Inr5oYttMK6J47vxgv6J&t=148
#     cur = con.cursor()

    # cur.executescript(""" CREATE TABLE IF NOT EXISTS cars (
    #     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     model TEXT NOT NULL,
    #     price INTEGER NOT NULL
    #     );
    #     CREATE TABLE IF NOT EXISTS cust (name TEXT, tr_in INTEGER, buy INTEGER);
    # """)

    # cur.execute("INSERT INTO cars VALUES(NULL, 'Запорожец', 1000)")
    # last_row_id = cur.lastrowid
    # buy_car_id = 2
    # cur.execute("INSERT INTO cust VALUES('Федор', ?, ?)", (last_row_id, buy_car_id))

    # cur.execute('SELECT model, price FROM cars')
    # #Для получения результатов SELECT'а списком
    # rows = cur.fetchall()
    # print(rows)

    # #Для получения результатов SELECT'а - только первая запись
    # rows = cur.fetchone()
    # print(rows)

    # #Для получения результатов SELECT'а - только кол-во записей указанного в скобках
    # rows = cur.fetchmany(4)
    # print(rows)

    # Перебор циклом - ПРЕИМУЩЕСТВО - экономия памяти
    # https://youtu.be/Ic6etzJZF-M?list=PLA0M1Bcd0w8x4Inr5oYttMK6J47vxgv6J&t=108
    # for result in cur:
    #     # print(result)
    #     # Для вывод данных в виде словаря: https://youtu.be/Ic6etzJZF-M?list=PLA0M1Bcd0w8x4Inr5oYttMK6J47vxgv6J&t=148
    #     print(result['model'], result['price'])


    # #Хранение изображений в БД:
    # #https://youtu.be/Ic6etzJZF-M?list=PLA0M1Bcd0w8x4Inr5oYttMK6J47vxgv6J&t=226

    # cur.executescript('''CREATE TABLE IF NOT EXISTS users2 (
    #     name TEXT,
    #     ava BLOB,
    #     score INTEGER)
    # ''')

    # #Функция записи изображений в БД:
    # def readAva(n):
    #     try:
    #         with open(f'E:\VSCode\Python_SQLite/{n}.png', 'rb') as f:
    #             return f.read()
    #     except IOError as e:
    #         print(e)
    #         return False

    # #Запись изображения в БД:
    # img = readAva(1)
    # if img:
    #     binary = sq.Binary(img)
    #     cur.execute("INSERT INTO users2 VALUES ('Exp010203', ?, 100)", (binary,))
    
    # #Чтение изображения из БД:
    # #Функция записи данных в виде графического файла
    # def writeAva(name, data):
    #     try:
    #         with open(name, 'wb') as f:
    #             f.write(data)
    #     except IOError as e:
    #         print(e)
    #         return False

    #     return True

    # #Чтение изображения из БД:
    # cur.execute("SELECT ava FROM users2 LIMIT 1")
    # img = cur.fetchone()['ava'] # обращаемся по имени, т.к. есть con.row_factory = sq.Row в функции with sq.connect, если её не было, то обращаемся по индексу (1/2/3...)

    # writeAva('out.png', img)

    # # Получить список SQL-запросов к БД - метод iterdamp()
    # #https://www.youtube.com/watch?v=Ic6etzJZF-M&list=PLA0M1Bcd0w8x4Inr5oYttMK6J47vxgv6J&index=11
    # # Простой просмотр запросов
    # for sql in con.iterdump():
    #     print(sql)

    # #Запись SQL-запросов в файл sql_dump.sql
    # with open('sql_dump.sql', 'w') as f:
    #     for sql in con.iterdump():
    #         f.write(sql)

    # #Создание/восстановление БД с помощью сохранённых SQL-запросов в файл sql_dump.sql
    # with open('sql_dump.sql', 'r') as f:
    #     sql in f.read()
    #     cur.executescript(sql)

    #Создание БД непосредственно в памяти ПК не создавая её физически в БД
    #https://youtu.be/Ic6etzJZF-M?list=PLA0M1Bcd0w8x4Inr5oYttMK6J47vxgv6J&t=641
data = [('car', 'машина'), ('house', 'дом'), ('thee', 'дерево'), ('color', 'цвет')]

con = sq.connect(':memory:')
with con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS dict(
        eng TEXT, rus TEXT
    )''')

    cur.executemany("INSERT INTO dict VALUES(?,?)", data)

    cur.execute("SELECT rus FROM dict WHERE eng LIKE 'c%'")
    print(cur.fetchall())