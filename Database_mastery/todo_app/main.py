import sqlite3

conn = sqlite3.connect('todo_data.db')

c = conn.cursor()

def add_task(task: int, day: str, month: str, year: str):
    pass





conn.commit()

conn.close()