import tkinter as tk
from tkinter import ttk
import mysql.connector

# database setup
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "necrons"
)

cursor = db.cursor()

# setup
app = tk.Tk()
app.geometry("1920x1080")

# widgets
cursor.execute("SELECT DATABASE()")
label_str = cursor.fetchone()[0].title()
label = ttk.Label(app, text = label_str)
label.pack()

combo = ttk.Combobox(app, values = label_str)
combo.pack()

# run
app.mainloop()