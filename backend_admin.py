import sqlite3
def connect():
    conn=sqlite3.connect("market.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS mar (lic INTEGER PRIMARY KEY,name text,weight integer,price integer,quan integer,offer integer,mfr text)")
    conn.commit()
    conn.close()

def insert(lic,name,weight,price,quan,offer,mfr):
        conn = sqlite3.connect("market.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO mar VALUES(?,?,?,?,?,?,?)", (lic,name,weight,price,quan,offer,mfr))
        conn.commit()
        conn.close()

def view():
    conn=sqlite3.connect("market.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM mar")
    rows=cur.fetchall()
    conn.close()
    return rows

def update(lic,name,weight,price,quan,offer,mfr):
    conn = sqlite3.connect("market.db")
    cur = conn.cursor()
    cur.execute("UPDATE mar SET name=?,weight=?,price=?,quan=?,offer=?,mfr=? WHERE lic=?",(name,weight,price,quan,offer,mfr,lic))
    conn.commit()
    conn.close()

def search(lic="",name=""):
    conn = sqlite3.connect("market.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM mar WHERE lic=? OR name=?",(lic,name))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(lic):
    conn = sqlite3.connect("market.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM mar WHERE lic=?",(lic,))
    conn.commit()
    conn.close()

connect()
print(view())