import pymysql
from flask_end_to_end_weekdays.helper.app_queries import *
#pymysql connector -->
def get_connection():   # this returns connection -- which ack with database
    return pymysql.connect(host=HOST,user=USERNAME,password=PASSWORD,database=DB_NAME, port=PORT)



if __name__ == '__main__':
    conn = get_connection()
    print(conn)