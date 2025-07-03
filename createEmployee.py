import mysql.connector

# Connection Establishment

conn = mysql.connector.connect(host='localhost',database='aug2024',user='root',password='root')

if conn.is_connected():
    print("Connection Established Successfully ")

cursor = conn.cursor()

try:
    cursor.execute("insert into emp values(106,'Ayan',99000)")
    cursor.execute("insert into emp values(107,'Shruti',98000)")
    cursor.execute("insert into emp values(103,'Mukesh',92000)")
    cursor.execute("insert into emp values(104,'Arif',97000)")
    # cursor.execute("insert into emp values(105,'Amit',99000)")

    conn.commit()
    print("Employee Added Successfully")
except:
    conn.rollback()

cursor.close()
conn.close()