
#  sqlite===>         mysql -- postgres

#--> exception handling --> -10 --> business not valid  --> all assignment-> custom exception --
#int(input('Enter ID')) --> raise-- INvalidEmpId    --> InvalidSalary --

#no of attempts --> 3 chances--> outof theapplication-->

# migrate- - file -- database--> csv -- excel --> json -->  all migrations---> emplist*-->

#1 File 2 Json  3 CSV  4 Excel  5 Database  6.Migrate       --> 6
    #1-5 -- 7                               6--> from - to
#1-5 --> 7 oprs -->                         6. -->  1 From     ->     2. To
                                                    #Mysql           file       --> file madhe
                                                    #json           database---> json to db

        #file --list-->database--write

from all_persist_ops.service import EmpService
from all_persist_ops.employee import Employee

CREATE_TABLE_SQL = '''create table EMP_INFO(emp_id int,emp_name varchar(40),emp_age int,emp_sal float,emp_role varchar(40),primary key(emp_id))'''
INSERT_RECORD_SQL = '''insert into emp_info values({},'{}',{},{},'{}')'''
DELETE_RECORD_SQL = '''delete from emp_info where emp_id={}'''
SELECT_ALL_SQL = '''select * from emp_info'''
SELECT_SINGLE_SQL = '''select * from emp_info where emp_id={}'''
UPDATE_RECORD_SQL = '''update emp_info set emp_name='{}',emp_age={},emp_sal={},emp_role='{}' where emp_id={} '''

DATABASE_QUERIES = {
        "CREATE_TABLE" : CREATE_TABLE_SQL,
        "INSERT_RECORD" : INSERT_RECORD_SQL,        #insert into emp_info values(101,'AAAA',22,2827.34,'SSE')
        "UPDATE_RECORD" : UPDATE_RECORD_SQL,        #update emp_info set emp_name='BBBB',emp_age=22,emp_sal=3838.45,emp_role='SSE' where emp_id=333
        "DELETE_RECORD" : DELETE_RECORD_SQL,        #delete from emp_info where emp_id=101
        "RETRIVE_ALL" : SELECT_ALL_SQL,             #select * from emp_info
        "RETRIVE_SINGLE" : SELECT_SINGLE_SQL,       #select * from emp_info where emp_id=120
}


import pymysql
# first of all we need to connect with database--> pip install pymysql


#building-- laptop -->  rooms --> services -->      room--loan      room-- accounting       --> laptop
#laptop -- > 65k + -->  3306 --> mysql software             machine1                                        machine
                    #  5432- - postgress                     machine2 ipaddress/hostname/domainname
                    # 1521 --> oracle                        port -->
                    #8080 --> http
                    # smtp -- 43
                    # ftp -- 21-->

def get_database_connection():
    #host=None, user=None, password="",database=None, port=3306     #mysql--3306    --> oracle-- 1521 --> postgres-- 5432
    try:
        conn = pymysql.connect(host='localhost',user='root',password='root',database='db1',port=3306)
        #print('connection established..',conn)
        return conn
    except BaseException as b:
        print(type(b))


def retrive_data_from_db(sql,many=True):
    conn = None  # local variable
    channel = None  # local variable        #conn --> pysql             --> cursor --> conn         --> sql--> cursor
    try:
        conn = get_database_connection()  # db ack-- handshaking-- with database
        channel = conn.cursor()  # thru ack- communication channel --> database sql
        channel.execute(sql)  # will run sql on datbase-->
        if many:
            return channel.fetchall()           # all records
        else:
            return channel.fetchone()           # fetch one
    except:
        print("problem in data fech")
    else:
        conn.commit()
    finally:
        if channel:
            channel.close()
        if conn:
            conn.close()


def establish_comm_channel(sql):# to pass sql/data/retrive--> from/db -- datbase-python
    conn = None     # local variable
    channel = None  # local variable        #conn --> pysql             --> cursor --> conn         --> sql--> cursor
    try:
        conn = get_database_connection()    # db ack-- handshaking-- with database
        channel = conn.cursor()             # thru ack- communication channel --> database sql
        channel.execute(sql)                # will run sql on datbase-->
    except :
        print("problem in query execution")
    else:
        conn.commit()
        return True     #operation successful..    deemed -- not an immediate impact--[try-->except--]     blocks la-->
    finally:
        if channel:
            channel.close()
        if conn:
            conn.close()



class EmpDBServiceImpl(EmpService):

    def create_table_for_emp(self):
        create_table_sql = DATABASE_QUERIES["CREATE_TABLE"]
        establish_comm_channel(create_table_sql)
        print('Table created ')

    def add_employee(self, emp):
        dbemp = self.get_employee(emp.empId)
        if dbemp:
            print('Duplicate employee record')
        else:
            insert_sql = DATABASE_QUERIES["INSERT_RECORD"]
            insert_sql = insert_sql.format(emp.empId,emp.empName,emp.empAge,emp.empSalary,emp.empRole)
            print(insert_sql)
            result = establish_comm_channel(insert_sql)
            if result==True:
                print('Emp information inserted successfully...!')

    def get_employee(self, empid):
        single_emp_sql = DATABASE_QUERIES["RETRIVE_SINGLE"]
        single_emp_sql = single_emp_sql.format(empid)
        #print(single_emp_sql)
        row = retrive_data_from_db(single_emp_sql, many=False)  #()
        if row:
            return Employee(eid=row[0],enm=row[1],eag=row[2],esal=row[3],erol=row[4])


    def get_all_employees(self):
        all_emp_sql = DATABASE_QUERIES["RETRIVE_ALL"]
        #print(all_emp_sql)
        rows = retrive_data_from_db(all_emp_sql,many=True)
        #print(allemps)
        emplist = []
        for row in rows:
            emplist.append(Employee(eid=row[0],enm=row[1],eag=row[2],esal=row[3],erol=row[4]))
        return emplist

    def delete_employee(self, empid):
        dbemp = self.get_employee(empid)
        if dbemp:
            delete_sql = DATABASE_QUERIES["DELETE_RECORD"]
            delete_sql = delete_sql.format(empid)
            print(delete_sql)
            result = establish_comm_channel(delete_sql)
            if result:
                print('Record deleted..')
        else:
            print('No record for delete..!')

    def update_employee(self, empid, emp):
        dbemp = self.get_employee(empid)
        if dbemp:
            update_sql = DATABASE_QUERIES["UPDATE_RECORD"]
            update_sql = update_sql.format(emp.empName, emp.empAge, emp.empSalary, emp.empRole,empid)
            result = establish_comm_channel(update_sql)
            if result==True:    # if result:
                print('Record updated..!')
        else:
            print('No record for update..!')

    def emp_avg_salary(self):
        ans = retrive_data_from_db('select avg(emp_sal) from emp_info',many=False)
        if ans:
            return round(ans[0],2)

    def get_rolebased_avg_salary(self,role):
        ans = retrive_data_from_db(f"select avg(emp_sal) from emp_info where emp_role='{role}'", many=False)
        #print(ans)
        if ans:
            return round(ans[0], 2)

    def get_employees_based_on_role(self, rolenm):
        rows = retrive_data_from_db(f"select * from emp_info where emp_role='{rolenm}'", many=True)
        emplist = []
        for row in rows:
            emplist.append(Employee(eid=row[0], enm=row[1], eag=row[2], esal=row[3], erol=row[4]))
        return emplist


from all_persist_ops.helper import get_input_from_user
if __name__ == '__main__':

    dbservice = EmpDBServiceImpl()
    #for item in range(3):
    #    emp = get_input_from_user(idwant=True)
    #    dbservice.add_employee(emp)
    #dbservice.update_employee(emp.empId,emp)
    #dbservice.create_table_for_emp()
    #import sys
    #sys.exit(0)
    #dbservice.delete_employee(102)
    #print(dbservice.get_all_employees())
    #print(dbservice.get_employee(101))
    #print(dbservice.emp_avg_salary())
    #print(dbservice.get_rolebased_avg_salary('Lead'))
    print(dbservice.get_employees_based_on_role('SE'))
    #
'''                        1            2              3            4
database software --> sqlite3       --> mysql               --> oracle  -       -> postgres
                        -               pymysql                 oracle_cx3           psychopg2
                                        mysql-connector
                                        mydbclient    


database --> lang -> sql --> structured 

CRUD -->

DATABASE SOFTWARES
                DATABASE-SCHEMAS
                            TABLES
                                    ROWS/COLUMNS
                                            DATA


MYSQL       --> DOWNLOAD AND DB SOFTWARE/--> 
        DB1 --> N TABLES    --> N ROWS/COLUNMS
        DB2
        DB3                                          







1 --> Python Provided --> No extra configuration required-->


2/3/4 --> We need download the software and install it..



DBSoftware              interface             Python            ---> lib
                        connector
                        api
                        bridge




what is Database -->            structure--> rows/columns-tables-> scehma[database]
Why Database -->

data is king-->*        pubg --> servers ?? data --? income ??
                        users data -->  **      --> user data--> user pattern--> processing--> dev/extend--
                                    game user base increase--> no of users--> income--*
                        advs -->    *
                        playstore downloads-->  *
                        addons -> win--> addicated--> power purchase--*payment

                        Flipkart --> ecom-->user--> pattern--> new business-->
                                 products--> Ele--cloths-house--
                                 user base increase--> user data--> can start any service---*
                                 --> insurance-->
                                 --> hostprovider
                                 --> loan related-->
                                 --> recharging
                                 --> ticketbook
                                 --> store
                                    users
                        Ola
                            Travelling  -- all data--> NOtification-->
                            Uber -->            ubereat
                                traveling   -->             --> feasible--*

    --> Permt storage -->           file??  process--> entire into memory--> file currupt-->
                                    entire process?? --> perfm slow ??
    --> Large Amount of data
    --> Structured Storage
    --> Efficient -- retrival/inseration/searching/deletion/modification
    --> better security


'''
