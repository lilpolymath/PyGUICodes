import sqlite3

def connect():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS animal (id INTEGER PRIMARY KEY, name text, owner text, kind text, age integer, arrival date, departure date, status text, comment text)")
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

connect()


# Examples
# insert("Gary", "Admin", "Dog", 8, "10-10-2018", "11-10-2018", "Treated", "Fine")
# insert("Stiles", "Philip", "Pig", 3, "12-10-2018", "12-10-2018", "Treated", "Fine")
# insert("Strong", "Pt. Timi", "Dog", 13, "12-10-2018", "14-10-2018", "Treated", "unknown")
# print(view())
# print("After the Update.")
# update(3, "Strong", "Pst. Timi", "Dog", 6, "12-10-2018", "14-10-2018", "Untreated", "unknown")
# print(view())
