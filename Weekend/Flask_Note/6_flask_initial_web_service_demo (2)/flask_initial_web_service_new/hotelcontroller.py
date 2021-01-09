from flask_initial_web_service_demo.model import *
from flask import Flask,request,render_template

@app.route('/hotel/',methods=['GET','POST'])
def hotel_page():
    return render_template('hotel.html')
