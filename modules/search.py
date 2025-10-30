import sqlite3

def search_by_type(file_type):
    conn = sqlite3.connect("files.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM files WHERE type=?", (file_type,))
    return cur.fetchall()

