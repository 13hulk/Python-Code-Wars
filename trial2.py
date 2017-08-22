import sqlite3

con = sqlite3.connect('tutorial.db')
cur = con.cursor()

def insert_data(line):
    cur.execute("INSERT INTO student_t (name, age, address) VALUES(?,?,?)", (line[0],line[1],line[2]))
    con.commit()

def read_file():
    f = open("input", 'r')

    for row in f.readlines():
        insert_data(row.split(','))
        #print(row.split(','))

def delete_data():
    cur.execute("DELETE FROM student_t")
    con.commit()

def fetch_data():
    for row in cur.execute("SELECT * FROM student_t"):
        print(row)

#delete_data()
#insert_data()
#read_file()
fetch_data()

con.close()