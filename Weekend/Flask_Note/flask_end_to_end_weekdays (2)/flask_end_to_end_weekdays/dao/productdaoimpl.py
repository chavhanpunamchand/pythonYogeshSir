from flask_end_to_end_weekdays.configurations.db_config import get_connection
from flask_end_to_end_weekdays.configurations.orm_config import db
from flask_end_to_end_weekdays.models.productinfo import Product
from functools import reduce
from sqlalchemy import or_,and_,any_,all_

class ProductDaoPlainQueriesImpl:   # efforts --> khup jast --> querires--> map--> con-col
    pass

class ProductDAOORMImpl:

    def add_product(self,prod):
        if type(self.get_product(prod.pid))==Product:
            return self.update_product(prod)
        else:
            try:
                db.session.add(prod)
                db.session.commit()
                return "Product recorded inserted Successfully...!"
            except:
                return "Problem in Product Add"

    def get_product(self,prid):
        try:
            prod = Product.query.filter_by(pid=prid).first()
            if prod:
                return prod
        except:
            return "Problem In Fetch Product "

        return "No Product with given ID "

    def get_all_products(self):
        prodlist= Product.query.all()
        prodlist.reverse()
        return prodlist
    
    def delete_product(self,prid):
        prod = self.get_product(prid)
        if type(prod) == Product:
            db.session.delete(prod)
            db.session.commit()
            return "Product Removed"
        else:
            return prod + ",cannot delete.."

    def update_product(self,user_given_prod):
        prod = self.get_product(user_given_prod.pid)
        if type(prod) == Product:
            prod.name = user_given_prod.name
            prod.qty = user_given_prod.qty
            prod.price = user_given_prod.price
            prod.cat = user_given_prod.cat
            db.session.commit()
            return "Product Updated Successfully..."
        else:
            return prod + ",Cannot Update"


    def total_inventory_investment(self):
        prods = self.get_all_products()
        if prods:  # reduce -- >    p1,p2 --> product,product   ---> 12.23,product
            finalans = reduce(lambda p1, p2: p1.price + p2.price if type(p1) == Product else p1 + p2.price)
            return finalans

'''
SQLALCHEMY QUERIES
    CREATE_TABLE -> DB_CREATEALL()
    DROP_TABLE   -> DB_DROPALL()
    INSERT      --> db.session.add(class instance who is child of db.model)  db.session.commit()
    DELETE      --> db.session.delete(class instance who is child of db.model)  db.session.commit()
    FETCH       --> Product.query.all()     --> all records
    FETCH_SINGLE -> Product.query.filter_by(pid=val).first()    #pk -query  assignement
                    Product.query.filter(name==val).first()     #npk -->    comparison
      
    from sqlalchemy import or_
    Product.query.filter(or_(Product.name=='AAA', Product.price>=100.0)).all() #OR
    Product.query.filter(and_(Product.name=='AAA', Product.price>=100.0)).all()#AND
    Product.query.filter(Product.name=='AAA', Product.price>=100.0).all() #AND
            where -->name or price              
            
            CND1 = OR_(Product.name=='AAA', Product.price>=100.0)   # OR
            CND1 = AND_(Product.name=='AAA', Product.price>=100.0)  #AND
            CND3 = AND_(Product.name=='AAA', Product.price>=100.0)  #AND
            FILTER(AND(CND1,CND2,CDN2))     #      
                    
'''