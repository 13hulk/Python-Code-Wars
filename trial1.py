import sqlite3

conn = sqlite3.connect('tutorial.db')

cur = conn.cursor()

def create_table():
    cur.execute("CREATE TABLE student_t(name VARCHAR, age INT, address TEXT)")
    conn.commit()

try:
    create_table()
except sqlite3.OperationalError:
    pass

def insert_data():
    name = input("Name: ")
    age = float(input("Age: "))
    address = input("Address: ")
    cur.execute("INSERT INTO student_t (name, age, address) VALUES(?,?,?)", (name, age, address))
    conn.commit()

#for i in range(3):
#insert_data()


def fetch_data():
    for row in cur.execute("SELECT * FROM student_t LIMIT 2"):
        print(row)

fetch_data()

conn.close()