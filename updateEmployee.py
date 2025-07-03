import mysql.connector

# Connection Establishment

conn = mysql.connector.connect(host='localhost',database='aug2024',user='root',password='root')

if conn.is_connected():
    print("Connection Established Successfully")

cursor = conn.cursor()

cursor.execute('select * from emp')

rows = cursor.fetchall()
print("Total number of records: ",cursor.rowcount)

sql = "update emp set name='Theja Payani' where name='Arif'"
cursor.execute(sql)
conn.commit()
print(f"{cursor.rowcount}, records effected")
cursor.close()
conn.close()