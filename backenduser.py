import sqlite3
def connectt():
    conn=sqlite3.connect("market.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS market (name TEXT PRIMARY KEY,weight integer,price integer,quan integer)")
    conn.commit()
    conn.close()

def insertt(name, weight, price, quan):
    conn = sqlite3.connect("market.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO market VALUES(?,?,?,?)", (name, weight, price, quan,))
    conn.commit()
    conn.close()

def vieww():
    conn=sqlite3.connect("market.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM market")
    rows=cur.fetchall()
    conn.close()
    return rows

def searchh(name="",weight=""):
    conn = sqlite3.connect("market.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM market WHERE name=? OR weight=?",(name,weight))
    rows = cur.fetchall()
    conn.close()
    return rows

connectt()
print(vieww())