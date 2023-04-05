import pyodbc
import random

number = random.randint(0, 195)

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\jadam\OneDrive\Documents\words.accdb;')
cursor = conn.cursor()
cursor.execute(f"SELECT words.word FROM words WHERE (((words.ID)={number}));")

for row in cursor.fetchall():
    word = str(row[0])

word_length = len(word)
