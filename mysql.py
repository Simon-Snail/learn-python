import mysql.connector

conn = mysql.connector.connect(user = 'root', password = 'root', database = 'snail')
cursor = conn.cursor()
cursor.execute('insert into user (id, name) values (%s, %s)' ['4', 'C'])
conn.commit()
cursor.close()
conn.close()