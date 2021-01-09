from flask_end_to_end_weekdays.configurations.orm_config import db



#python fields --------------> database table columns
# sqlalchemy always adds init with all fields --> instance fields -->
class Product(db.Model):        # model --> class going to represent python fields-- which we are going to map it to the table-
    pid = db.Column('prod_id', db.Integer(),primary_key=True)
    name = db.Column('prod_name',db.String(100))
    qty = db.Column('prod_qty',db.Integer())
    price = db.Column('prod_price', db.Float())
    cat = db.Column('prod_cat', db.String(100))
    vendor = db.Column('prod_ven', db.String(100))
    active = db.Column('active', db.String(5),default="Y")
    created = db.Column('created', db.DateTime,  default=db.func.current_timestamp())  # date type --> when this record added into db
    updated= db.Column('updated', db.DateTime,  default=db.func.current_timestamp(),onupdate=db.func.current_timestamp())   # date type --> when last time updated
    created_by = db.Column('created_by', db.Integer(),default=0)  # who created
    updated_by = db.Column('updated_by', db.Integer(),default=0)  # who last time updated

    @staticmethod
    def get_dummy_product():
        return Product(pid=0,name='',qty=0,price=0.0,cat='',vendor='')

    def __str__(self):
        return f'''\nPID : {self.pid} Name : {self.name} Price : {self.price} Qty :{self.qty} Vender :{self.vendor} Created :{self.created} Updated :{self.updated}'''

    def __repr__(self):
        return str(self)


import sys
import time
if __name__ == '__main__':
    #update_product(Product(pid=101, name='PPPP', qty=42, price=1223.34, cat='A+', vendor='Flipkart'))
    sys.exit(0)
    db.create_all()
    for item in range(10):
        add_product(Product(pid=101+item,name=f'AAA{item}',qty=12+item,price=1223.34+item,cat='A+',vendor='Flipkart'))
    print('all product added successfully...')
    print('waiting')
    time.sleep(10)
    update_product(Product(pid=101, name='TTTT', qty=42, price=1223.34, cat='A+', vendor='Flipkart'))

    #db.drop_all()   # remove entire data -->
    #sys.exit(0)

    #delete_product(101)

    #update_product(Product(pid=101,name='TTTT',qty=42,price=1223.34,cat='A+',vendor='Flipkart'))

    #print(get_product(112))
    sys.exit(0)
    print(get_all_products())


    for item in range(10):
        add_product(Product(pid=103+item,name=f'AAA{item}',qty=12+item,price=1223.34+item,cat='A+',vendor='Flipkart'))
    #db.create_all() # sqlal--> all models --> class -> db.model --> child --> tables-->
    #pr1 =Product(pid=101,name='PAAA',qty=12,price=1223.34,cat='A+',vendor='Flipkart')
    #db.session.add(pr1) # insert query --> sqlachemy -->
    #db.session.commit()