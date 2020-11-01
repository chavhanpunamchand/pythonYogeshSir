import sqlite3

def get_connection():       # software --> python -la --> communication --> connection
    return sqlite3.connect('products.db')


#database lang-- https://www.tutorialspoint.com/sqlite/sqlite_python.htm --> read this till next session

def add_product_into_db():
    pass

def delete_prod_from_db():
    pass

def get_prod_from_db():
    pass

def update_product_into_db():
    pass

def get_all_products():
    pass


conn = get_connection()
print(conn)