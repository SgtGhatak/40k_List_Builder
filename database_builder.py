import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "necrons"
)

cursor = db.cursor()

#cursor.execute("CREATE DATABASE necrons")

#cursor.execute("CREATE TABLE necron_unit (name VARCHAR(255) PRIMARY KEY, movement INT, toughness INT, save INT, wounds INT, leadership INT, objective_control INT)")

# sql = "INSERT INTO necron_unit (name, movement, toughness, save, wounds, leadership, objective_control) VALUES (%s, %s, %s, %s, %s, %s, %s)"
# value = [
#     ("Necron Warriors", 5, 4, 4, 1, 7, 2),
#     ("Immortals", 5, 5, 3, 1, 7 , 2),
#     ("Cryptothralls", 5, 4, 3, 3, 8, 1),
#     ("Deathmarks", 5, 5, 3, 1, 7, 1),
#     ("Flayed Ones", 5, 3, 3, 1, 7, 1),
#     ("Lychguard", 5, 5, 3, 2, 7, 1),
#     ("Ophydian Destroyers", 10, 5, 4, 3, 7, 2),
#     ("Skorpekh Destoryers", 8, 6, 3, 3, 7, 2),
#     ("Triarch Praetorians", 10, 5, 3, 2, 7, 1)
# ]
# cursor.executemany(sql, value)

# db.commit()

# print(cursor.rowcount, "record inserted.")

cursor.execute("SELECT name FROM necron_unit")

result = cursor.fetchall()

# cursor.execute("SHOW TABLES")

for x in result:
    print(x)
