import mysql.connector
from mysql.connector import Error
 
 
def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='force@ec2-52-87-182-66.compute-1.amazonaws.com',
                                       database='choices',
                                       user='root',
                                       password='secret')
        if conn.is_connected():
            print('Connected to MySQL database')
 
    except Error as e:
        print(e)
 
    finally:
        conn.close()
 
 
if __name__ == '__main__':
    connect()

# ssh -i team12.pem force@ec2-52-87-182-66.compute-1.amazonaws.com