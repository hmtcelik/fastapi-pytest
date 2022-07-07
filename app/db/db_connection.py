import sqlite3

def connection():
    try:
        con = sqlite3.connect('./sql_app.db')
        return con
    except Exception as e:
        print(e)