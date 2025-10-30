import os, hashlib, sqlite3, time

def sha256_checksum(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

def create_db():
    conn = sqlite3.connect("files.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS files(
        path TEXT, name TEXT, size INTEGER, type TEXT,
        created REAL, modified REAL, checksum TEXT
    )""")
    conn.commit()
    conn.close()

def scan_directory(directory):
    create_db()
    conn = sqlite3.connect("files.db")
    cur = conn.cursor()

    for root, _, files in os.walk(directory):
        for f in files:
            file_path = os.path.join(root, f)
            size = os.path.getsize(file_path)
            created = os.path.getctime(file_path)
            modified = os.path.getmtime(file_path)
            ext = os.path.splitext(f)[1]
            checksum = sha256_checksum(file_path)

            cur.execute("INSERT INTO files VALUES (?,?,?,?,?,?,?)",
                        (file_path, f, size, ext, created, modified, checksum))
            conn.commit()
    
    conn.close()

