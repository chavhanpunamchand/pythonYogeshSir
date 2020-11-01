'''
42
You get a UNIQUE constraint failed error when the data that you are inserting has an entry which is already
in the corresponding column of the table that you are inserting into.

'''
class Product:
    def __init__(self,pid,pnm,pri,pqty,pbar):
        self.prodId = pid
        self.prodName = pnm
        self.prodPrice = pri
        self.prodQty = pqty
        self.prodCode = pbar

    def __repr__(self):
        return str(self)

    def __str__(self):                      #self -- current object ref--       self.__dict__   --> {prodId:101,}
        prodcontents = ''       #create dynamic-- string- based on object properties
        for propname,propvalue in self.__dict__.items():
            prodcontents = "\n"+prodcontents + propname +":" +str(propvalue)+"\n"
        return prodcontents     # all properties-- with thr values--\n


#rest api -- webservices--> json ---> json format-->

#print(products)

import sqlite3  # python provided database-->       lightweight-> no installation--> directly plugin

connection = None
def get_connection():
    global connection
    try:
        connection = sqlite3.connect('prod.db') # file acccess--> ack
        if connection:
            return connection
    except:
        print('Problem in creating connection')


CREATE_TABLE_SQLITE = '''
                CREATE TABLE PRODUCT_INFO(
                   ID INT PRIMARY KEY     NOT NULL,
                   PROD_NAME           TEXT    NOT NULL,
                   PROD_QTY            INT     NOT NULL,
                   PROD_CODE        CHAR(50),
                   PROD_PRICE         REAL
                )
            '''

def create_table_into_sqlite3():
    conn = get_connection()
    cursor = conn.cursor()  # u can fire queries--> sql -->  database lang-->
    cursor.execute(CREATE_TABLE_SQLITE)
    conn.commit()

def insert_product(prod):
    INSERT_PRODUCT_INTO_SQLITE3 = f"INSERT INTO PRODUCT_INFO VALUES({prod.prodId},'{prod.prodName}',{prod.prodQty},'{prod.prodCode}',{prod.prodPrice})"
    conn = get_connection()  # this is for -- opt connection for sqlite3 database
    try:
        cursor = conn.cursor()
        cursor.execute(INSERT_PRODUCT_INTO_SQLITE3)
        conn.commit()
    except BaseException as e:     # to handle exception -- Baseexception
        print('not inserted..',e.args)
    finally:            # resource cleanup--
        if conn:
            conn.close()

# create_table_into_sqlite3() # table --> 5 columns --> id prod_name prod_Qty prod_Code prod_price
#create_table_into_sqlite3()

def get_filteredproducts(qty):
    sql = 'select * from product_info where prod_qty>{}'.format(qty)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    print(cursor.fetchall()) # to get all records from resultset--
    conn.close()        # finally block madhe--> as it gets executed always.
#get_filteredproducts(33)    # performance better

# get --> write -->     crud --> create -- read  update  -- delete

def delete_record(pid):
    sql = 'delete from product_info where id={}'.format(pid)
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()

def update_product(pid,values): #101 values-- product
    sql = f'''update product_info set prod_name='{values.prodName}',prod_qty={values.prodQty},prod_price={values.prodPrice},prod_code='{values.prodCode}' where id={pid}'''
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()

item  = 100
p1 = Product(102+item,"TV",25000.5,2,'ThinkPad')  #python object--> to be converted into json
print(p1)

update_product(110,p1)  #

# delete_record(102)
# import sys
# sys.exit(0)
products = []
for item in range(10):
    p1 = Product(102+item,"AAAA"+str(item),2929.34+item,27+item,'A{}XXX'.format(item))  #python object--> to be converted into json
    products.append(p1)

for prod in products:
    insert_product(prod)


import sys
sys.exit(0)

#database --> sql --> structure query lang -->
# create table table --
# insert into tablename values-->

#corp --> 8 hrs --> mysql -- env specific -->
        #python --> database --> sqlite3--> python --> no extra configuration --> inbuild-- no setup-->

# database  --> file format --> txt excel json  csv xml --> searching/sorting--> query --> search criteria-->
                    #--> file corrupt
                    #--> file  security ??  --> kah access --?? not access-->
                    #--> n database -->