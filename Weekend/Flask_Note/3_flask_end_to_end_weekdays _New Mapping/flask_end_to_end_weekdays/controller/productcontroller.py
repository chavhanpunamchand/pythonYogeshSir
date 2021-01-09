from flask import Flask,request,render_template
from flask_end_to_end_weekdays.configurations.app_config import app
from flask_end_to_end_weekdays.models.productinfo import Product
from flask_end_to_end_weekdays.dao.productdaoimpl import ProductDAOORMImpl

dbop = ProductDAOORMImpl()

@app.route("/index/",methods=['GET'])   #http://localhost:5000/index/ --GET
def welcom_page():
    return render_template('product.html',prodlist = dbop.get_all_products(),prod=Product.get_dummy_product())

@app.route("/persist/",methods=['POST']) #http://localhost:5000/persist/ --post--> request.form
def add_update_product_info():
    formdata = request.form # method type is --> post
    values = formdata.getlist('pcat')   #A,C
    vals = ''
    for val in values:
        vals = vals+","+val
    pr = Product(pid=formdata.get('pid'),
            name=formdata.get('pname'),
            qty=formdata.get('pqty'),
            price=formdata.get('pprice'),
            cat=vals,
            vendor=formdata.get('pven'))
    msg = dbop.add_product(pr)    # pr --> pass --> daoimpl
    return render_template('product.html',resp = msg,prodlist = dbop.get_all_products(),prod=Product.get_dummy_product())

@app.route("/edit/<int:pid>",methods=['GET'])       ##http://localhost:5000/edit/101 --GET -->pathvariable
def edit_product_info(pid):

    return render_template('product.html',prodlist = dbop.get_all_products(),prod = dbop.get_product(pid),resp='')

@app.route("/delete/<int:pid>",methods=['GET']) #http://localhost:5000/delete/101 --GET
def delete_product_info(pid):
    msg = dbop.delete_product(pid)
    return render_template('product.html',prodlist = dbop.get_all_products(),prod=Product.get_dummy_product(),resp=msg)




