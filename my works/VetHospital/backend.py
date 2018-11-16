import sqlite3

def connect():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS animal (id INTEGER PRIMARY KEY, name text, owner text, kind text, age integer, arrival text, departure text, status text, comment text)")
    conn.commit()
    conn.close()

def insert(name, owner, kind, age, arrival, departure, status, comment):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO animal VALUES (NULL, ?,?,?,?,?,?,?,?)", (name, owner, kind, age, arrival, departure, status, comment))
    conn.commit()
    conn.close()
    view()

def view():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM animal")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(name = "", owner = "", kind = "", age = "", arrival = "", departure = "", status = "", comment = ""):
    conn=sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM animal WHERE name=? OR owner=? OR kind=? OR age=? OR arrival=? OR departure=? OR status=? OR comment=?", (name, owner, kind, age, arrival, departure, status, comment))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM animal WHERE id = ?",(id,))
    conn.commit()
    conn.close()

def update(id, name, owner, kind, age, arrival, departure, status, comment):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("UPDATE animal SET name=?, owner=?, kind=?, age=?, arrival=?, departure=?, status=?, comment=? WHERE id = ?", (name, owner, kind, age, arrival, departure, status, comment, id))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    connect()

