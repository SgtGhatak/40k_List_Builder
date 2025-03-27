import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "necrons"
)

cursor = db.cursor()

#cursor.execute("CREATE DATABASE necrons")

cursor.execute("DROP TABLE necron_weapons")
cursor.execute("DROP TABLE necron_unit")

cursor.execute("CREATE TABLE necron_unit (unit_name VARCHAR(255) PRIMARY KEY NOT NULL, movement INT NOT NULL, toughness INT NOT NULL, save INT NOT NULL, wounds INT NOT NULL, leadership INT NOT NULL, objective_control INT NOT NULL)")

sql = "INSERT INTO necron_unit (unit_name, movement, toughness, save, wounds, leadership, objective_control) VALUES (%s, %s, %s, %s, %s, %s, %s)"
value = [
    ("Necron Warriors", 5, 4, 4, 1, 7, 2),
    ("Immortals", 5, 5, 3, 1, 7 , 2),
    ("Cryptothralls", 5, 4, 3, 3, 8, 1),
    ("Deathmarks", 5, 5, 3, 1, 7, 1),
    ("Flayed Ones", 5, 3, 3, 1, 7, 1),
    ("Lychguard", 5, 5, 3, 2, 7, 1),
    ("Ophydian Destroyers", 10, 5, 4, 3, 7, 2),
    ("Skorpekh Destoryers", 8, 6, 3, 3, 7, 2),
    ("Triarch Praetorians", 10, 5, 3, 2, 7, 1)
]
cursor.executemany(sql, value)

cursor.execute("CREATE TABLE necron_weapons (weapon_name VARCHAR(255) NOT NULL, attacks INT NOT NULL, bsws INT NOT NULL, strength INT NOT NULL, ap INT NOT NULL, damage INT NOT NULL, unit VARCHAR(255), FOREIGN KEY (unit) REFERENCES necron_unit(unit_name), PRIMARY KEY (weapon_name, unit))")

sql = "INSERT INTO necron_weapons (weapon_name, attacks, bsws, strength, ap, damage, unit) VALUES (%s, %s, %s, %s, %s, %s, %s)"
value = [
    ("Gauss flayer", 1, 4, 4, 0, 1, "Necron Warriors"),
    ("Gauss reaper", 2, 4, 4, -1, 1, "Necron Warriors"),
    ("Close combat weapon", 1, 4, 4, 0, 1, "Necron Warriors"),
    ("Gauss blaster", 2, 3, 5, 1, 1, "Immortals"),
    ("Tesla carbine", 2, 3, 5, 0, 1, "Immortals"),
    ("Close combat weapon", 2, 3, 4, 0, 1, "Immortals")
]
cursor.executemany(sql, value)

db.commit()

# print(cursor.rowcount, "record inserted.")

# cursor.execute("SELECT * FROM necron_unit")
cursor.execute("SELECT * FROM necron_unit JOIN necron_weapons ON necron_weapons.unit = necron_unit.unit_name")

result = cursor.fetchall()

# cursor.execute("SHOW TABLES")

for x in result:
    print(x)
