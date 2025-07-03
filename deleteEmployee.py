import mysql.connector

# Connection Establishment
def delete(id):
    conn = mysql.connector.connect(host='localhost',database='aug2024',user='root',password='root')

    if conn.is_connected():
        print("Connection Established Successfully")

    cursor = conn.cursor()

    # str = "delete from emp where id = '%d'"
    # args = (id)
    sql = f"delete from emp where id = {id}"
    try:
        # cursor.execute(str % args)
        cursor.execute(sql)
        conn.commit()
        print(f"Employee deleted successfully")
    except:
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

empID = int(input("Enter id to be deleted: "))
delete(empID)
