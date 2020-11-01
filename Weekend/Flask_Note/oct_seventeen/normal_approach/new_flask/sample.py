from flask import Flask,render_template,request

app = Flask(__name__)




@app.route("/emp/register") #http://localhost:5000/emp/register
def emp_info():
    return render_template('new.html')

@app.route("/emp/save/",methods=['POST'])
def save_employee_info():                       # info.get('eid)        info['eid']         {{info['eid']}}
    print('Ur Data --',request.form)        # immutablemultidict --> type ??? - NO --> flask ne--> dict -->
    return render_template('success.html',info = request.form,value = {"name":"Yogesh","email":"yogymax"})      #info





class Emp:
    def __init__(self,eid,enm):
        self.empId = eid
        self.empName = enm
    def __str__(self):
        return  f'''Emp Id : {self.empId} , Emp Name : {self.empName}'''


@app.route("/str")
def welcome_to_flask_web_app(): #http://localhost:5000/str
    return render_template('register.html',val = 'This is flask web app')


@app.route("/list")     #http://localhost:5000/list
def returnlist():
    return render_template('register.html',values = [10,20,30,40])

@app.route("/emp")  #http://localhost:5000/emp
def returnEmp():
    return render_template('register.html', empob = Emp(101,"Mr . AAAAA"))

@app.route("/all")
def all_values():
    return render_template('register.html',
                            empob=Emp(101, "Mr . AAAAA"),
                            values = [10,20,30,40],
                            val = 'This is flask web app')


if __name__ == '__main__':
    app.run(debug=True)

'''

 #not from html --> flask -- jinja template -->  jinja--flask -- python -- python list -->
    {{}}        # this is to print variable value       
    {% %}       #statement --> {% for item in range(10)%} {% if %}
    {# #}       # comments ->

'''