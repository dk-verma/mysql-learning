import mysql.connector

# Connection Establishment

conn = mysql.connector.connect(host='localhost',database='aug2024',user='root',password='root')

if conn.is_connected():
    print("Connection Established Successfully")

# FETCH ONE (Fetching One row)

cursor = conn.cursor()

cursor.execute('select * from emp')

row = cursor.fetchone()

# while row is not None:
    # print(row)
    # row = cursor.fetchone()

print("Using FETCH ONE : ", row)

# FETCH ALL (Fetching all remaining rows)

# cursor = conn.cursor()

# cursor.execute('select * from emp')

rows = cursor.fetchall()
print("Total number of records: ",cursor.rowcount)

print("Using FETCH ALL : ", rows)

# for row in rows:
    # print(row)

cursor.close()
conn.close()