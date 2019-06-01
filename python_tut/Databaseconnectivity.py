import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(host='localhost',
                            database='python_DB',
                            user='root',
                            password='')  
    if connection.is_connected():

        sql='''CREATE TABLE IF NOT EXISTS tasks (
             task_id INT AUTO_INCREMENT, 
            title VARCHAR(255) NOT NULL, 
            start_date DATE, 
             due_date DATE, 
            status TINYINT NOT NULL, 
            priority TINYINT NOT NULL, 
             description TEXT,
             PRIMARY KEY (task_id) ) '''
        print (sql)
        cursor = connection.cursor()
        cursor.execute(sql)
        
except Error as e :
    print ("Error while connecting to MySQL", e)
finally:
        #closing database connection.
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")