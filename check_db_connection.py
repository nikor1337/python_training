import mysql.connector

connection = mysql.connector.connect(host="192.168.1.69", database="addressbook", user="admin", password="admin")

try:
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()