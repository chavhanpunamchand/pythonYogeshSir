from flask import Flask,render_template,request

app = Flask(__name__)

#http://localhost:5000/index    --> address bar --> first time --> GET
@app.route("/index")        # method type method mentioned ??--No ---> GET
def welcome_page():
    return render_template('sample.html')

@app.route("/hello/<int:empid>")
def return_hello(empid):
    print('u clicked on {}'.format(empid))  #pathvariable
    return render_template('sample.html')

@app.route('/emp/save/')
def form_data():
    print("GET DATA",request.args)
    print('POST DATA',request.form)
    return render_template('sample.html')
    
@app.route('/emp/save/',methods=['POST'])
def form_data_info():
    print("GET DATA",request.args)
    print('POST DATA',request.form)
    return render_template('sample.html')



if __name__ == '__main__':
    app.run(debug=True)