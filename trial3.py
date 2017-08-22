import sqlite3

con = sqlite3.connect('tutorial.db')
cur = con.cursor()

def fetch_data():
    f = open("output", 'a')
    for row in cur.execute("SELECT * FROM student_t"):
        rlist = list(row)
        for i in rlist:
            try:
                f.write(i)
            except TypeError:
                f.write(str(i))
            f.write(',')
    f.close()


fetch_data()