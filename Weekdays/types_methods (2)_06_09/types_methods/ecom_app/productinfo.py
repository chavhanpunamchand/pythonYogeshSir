
'''
Types of variables
Types of methods
Types of params
Loopings- - selective iterative transfer
exception handling --> try except else finally

--> database  --> conn --> finally --> block-->
    data --> persist -->  database --> file -->


database file handling --> Exception handling --> loopings - integrate -->
'''


class Product:
    def __init__(self,pid,pnm,pri,pqty,prem,pcat):
        self.prodId = pid
        self.prodName = pnm
        self.prodPrice = pri
        self.prodQty = pqty
        self.prodRemarks = prem
        self.prodCategories = pcat

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)


productInventory = []       # same id chec 2 products ??? -- no


def get_with_attempts(no=3):
    for item in range(no):       #0  1  2
        try:
            no1 = int(input('Enter Product Id  : '))
            return no1
        except:
            print('Invalid Number')

    print('Attempt Exceeds...!')

def get_proper_product_name():
    for item in range(3):
        nm = input('Enter Product Name')
        if len(nm)>=5:
            return nm

import random
def get_user_input():
    id = get_with_attempts(5)
    if id:
        nm = get_proper_product_name()
        if nm:
            return Product(pid=id,pnm=nm,pri= random.randint(1000,3000),pqty=random.randint(1,10),prem='XX',pcat='ETC')
    else:
        print('Invalid Product values...!')


def add_new_product(prod):
    if type(prod)==Product:
        listprod = fetch_product(prod.prodId)
        if listprod:
            return "Duplicate Product"
        else:
            productInventory.append(prod)
            return "Product Added Successfully..."

    return "Invalid Product"

def delete_product(prodId):
    if type(prodId)==int and prodId>0:
        listprod = fetch_product(prodId)
        if listprod:
            productInventory.remove(listprod)
            return "Product Removed Successfully..."
        return "No product with give Identifier..!"
    return "Invalid Product Id..!"

def fetch_product(pId):     # pid
    if type(pId) == int and pId>0:      #pid--int  and >0
        for prod in productInventory:       #list iterate
            if prod.prodId == pId:          #prod.id --> pid --> return prod
                return prod
    return False

def fetch_all_products():
    if productInventory:
        return productInventory
    return "No Products"

def update_product(pid,toupdate):
    listProd = fetch_product(pid)
    if listProd:
        listProd.prodName = toupdate.prodName
        listProd.prodQty = toupdate.prodQty
        listProd.prodPrice = toupdate.prodPrice
        return "Product Updated"
    return "No Product found with given id or invalid Id"


while True:
    print('''
            1. Add Product 
            2. Update Product
            3. Delete Product
            4. Get Single Product
            5. Get All Product
    ''')

    choice = int(input('Enter Your Choice : '))     # 55

    operations =   {
                    1:add_new_product,
                    2:update_product,
                    3:delete_product,
                    4:fetch_product,
                    5:fetch_all_products
    }
    funref = operations.get(choice)      # 1--> getallref-->        1-->add_new_student
    if funref:
        prod = get_user_input()
        if prod:
            val = funref(prod)
            print(val)
    else:
        print('Invalid Choice...!')

    ch = input('Do you want to continue --> Yes/No  :  ')
    if ch.lower() not in ["y","yes"]:
        break

    print('----------------------------------------------')

import sys
sys.exit(0)
