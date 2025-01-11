import sqlite3

# Підключення до бази даних
connection = sqlite3.connect("database.sqlite")
cursor = sqlite3.Cursor(connection)

# Видалення старої таблиці (якщо вона існує) для тестування
cursor.execute("DROP TABLE IF EXISTS products")

# Створення таблиці products, додано нове поле image_name
request = ("CREATE TABLE IF NOT EXISTS products"
           "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
           "name VARCHAR(255),"
           "price INTEGER,"
           "image_name VARCHAR(255),"
           "image_name2 VARCHAR(255),"
           "image_name3 VARCHAR(255))")
cursor.execute(request)

# Вставка даних у таблицю products з новим полем image_name
insert_request = ("INSERT INTO products"
                  "(name, price, image_name, image_name2, image_name3) VALUES (?, ?, ?, ?, ?)")

cursor.execute(insert_request, ("Turismo R", 2525000, "turismo.jpg", "Turismo2.jpg", "Turismo3.jpg"))
cursor.execute(insert_request, ("Declasse Impaler LX", 3600000, "Car2.jpg", "car21.jpg", "car22.jpg"))
cursor.execute(insert_request, ("Scramjet", 2700000, "Car3.jpg", "car31.jpg", "car32.jpg"))
cursor.execute(insert_request, ("Vigilante", 2700000, "Car4.jpg", "car41.jpg", "car42.jpg"))
cursor.execute(insert_request, ("Coil Rocket Voil ZX", 4000000, "Car5.jpg", "car51.jpg", "car52.jpg"))
cursor.execute(insert_request, ("Ubermacht", 610000, "Car6.jpg", "car61.jpg", "car62.jpg"))

# Виведення всіх товарів з таблиці products
text = cursor.execute("SELECT * FROM products")
print("Товари в базі даних:")
for line in text.fetchall():
    print(line)

# Збереження змін та закриття з'єднання
connection.commit()
connection.close()